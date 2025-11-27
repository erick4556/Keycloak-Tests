#!/usr/bin/env python3
"""
Script para habilitar 2FA (TOTP) para un usuario específico en Keycloak.
Uso: python3 enable-2fa-user.py <username>
"""

import sys
import requests
import json

KEYCLOAK_URL = "http://localhost:8081"
REALM = "unified-realm"
ADMIN_USER = "admin"
ADMIN_PASSWORD = "admin"

def get_admin_token():
    """Obtiene un token de administrador de Keycloak"""
    url = f"{KEYCLOAK_URL}/realms/master/protocol/openid-connect/token"
    data = {
        "grant_type": "password",
        "client_id": "admin-cli",
        "username": ADMIN_USER,
        "password": ADMIN_PASSWORD
    }
    response = requests.post(url, data=data)
    if response.status_code != 200:
        raise Exception(f"Error obteniendo token: {response.status_code} - {response.text}")
    return response.json()["access_token"]

def get_user_id(token, username):
    """Obtiene el ID de un usuario por su username"""
    url = f"{KEYCLOAK_URL}/admin/realms/{REALM}/users"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"username": username, "exact": "true"}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Error buscando usuario: {response.status_code} - {response.text}")
    users = response.json()
    if not users:
        raise Exception(f"Usuario '{username}' no encontrado")
    return users[0]["id"]

def add_required_action(token, user_id, action="CONFIGURE_TOTP"):
    """Agrega una required action a un usuario"""
    url = f"{KEYCLOAK_URL}/admin/realms/{REALM}/users/{user_id}/execute-actions-email"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = [action]
    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 204:
        print(f"✅ Required action '{action}' agregada al usuario. Se enviará un email para configurar 2FA.")
        return True
    elif response.status_code == 200:
        print(f"✅ Required action '{action}' agregada al usuario.")
        return True
    else:
        print(f"⚠️  Respuesta inesperada: {response.status_code} - {response.text}")
        return False

def add_required_action_direct(token, user_id, action="CONFIGURE_TOTP"):
    """Agrega una required action directamente al usuario (sin email)"""
    # Primero obtenemos el usuario
    url = f"{KEYCLOAK_URL}/admin/realms/{REALM}/users/{user_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error obteniendo usuario: {response.status_code} - {response.text}")
    
    user = response.json()
    
    # Agregamos la required action si no está presente
    if "requiredActions" not in user:
        user["requiredActions"] = []
    
    if action not in user["requiredActions"]:
        user["requiredActions"].append(action)
        
        # Actualizamos el usuario
        update_url = f"{KEYCLOAK_URL}/admin/realms/{REALM}/users/{user_id}"
        update_headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        update_response = requests.put(update_url, headers=update_headers, json=user)
        if update_response.status_code == 204:
            print(f"✅ Required action '{action}' agregada directamente al usuario.")
            print(f"   El usuario deberá configurar 2FA en su próximo login.")
            return True
        else:
            raise Exception(f"Error actualizando usuario: {update_response.status_code} - {update_response.text}")
    else:
        print(f"ℹ️  El usuario ya tiene la required action '{action}' configurada.")
        return True

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 enable-2fa-user.py <username> [--email]")
        print("  --email: Envía un email al usuario para configurar 2FA")
        sys.exit(1)
    
    username = sys.argv[1]
    use_email = "--email" in sys.argv
    
    try:
        print(f"🔐 Habilitando 2FA para usuario: {username}")
        print(f"   Realm: {REALM}")
        print(f"   Keycloak: {KEYCLOAK_URL}")
        print()
        
        # Obtener token de admin
        print("1. Obteniendo token de administrador...")
        token = get_admin_token()
        print("   ✅ Token obtenido")
        
        # Buscar usuario
        print(f"2. Buscando usuario '{username}'...")
        user_id = get_user_id(token, username)
        print(f"   ✅ Usuario encontrado (ID: {user_id})")
        
        # Agregar required action
        print("3. Agregando required action CONFIGURE_TOTP...")
        if use_email:
            add_required_action(token, user_id)
        else:
            add_required_action_direct(token, user_id)
        
        print()
        print("✅ Proceso completado!")
        print()
        print("📋 Próximos pasos:")
        print("   1. El usuario debe iniciar sesión en cualquier aplicación")
        print("   2. Keycloak le pedirá configurar 2FA (TOTP)")
        print("   3. El usuario debe escanear el código QR con una app como Google Authenticator")
        print("   4. Ingresar el código de verificación")
        print("   5. A partir de entonces, cada login requerirá el código TOTP")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

