# Keycloak Demo - Use Cases

This project contains the implementation of different use cases for Keycloak in the context of identification and authentication.

## Project Structure

```
keycloak-demo/
├── USE_CASES.md              # Main document with all use cases
├── README.md                 # This file
├── AUTHENTICATION_GLOSSARY.md # Authentication terms glossary
├── use-cases/                # Folder with all use cases
│   ├── USE_CASE_1/            # SSO in corporate and citizen applications
│   ├── USE_CASE_2/            # Machine authentication - WEB services - Secrets vault
│   └── USE_CASE_3/            # Citizen identification (external repo)
└── [shared configuration files]
```

## Use Cases

See [USE_CASES.md](./USE_CASES.md) for the complete description of all use cases.

### USE_CASE_1: SSO in Corporate and Citizen Applications ✅

**Status**: Done

**Location**: `use-cases/USE_CASE_1/`

**Description**: Implementation of Single Sign-On (SSO) for corporate applications and also for citizens. A unified realm allows employees and citizens to authenticate once and access all their respective applications.

**To run**:
```bash
cd use-cases/USE_CASE_1
docker-compose up -d
```

See [use-cases/USE_CASE_1/README.md](./use-cases/USE_CASE_1/README.md) for more details.

---

### USE_CASE_2: Machine Authentication - WEB Services - Secrets Vault ✅

**Status**: Done

**Location**: `use-cases/USE_CASE_2/`

**Description**: Service-to-service authentication using Keycloak Client Credentials Grant, with secrets managed by Passbolt (GPG-authenticated vault). App X retrieves credentials from Passbolt, obtains a Keycloak token, and calls the protected App Z API.

**To run**:
```bash
cd use-cases/USE_CASE_2
docker-compose up -d
```

See [use-cases/USE_CASE_2/README.md](./use-cases/USE_CASE_2/README.md) for more details.

---

### USE_CASE_3: Citizen Identification ✅

**Status**: Done

**Location**: `use-cases/USE_CASE_3/`

**Description**: Citizen identification for natural persons, legal persons, and European persons using electronic certificate and Cl@ve system. This use case is implemented in an external repository.

**Repository**: [https://github.com/manabcodes/Keycloak-Tests-7](https://github.com/manabcodes/Keycloak-Tests-7)

See [use-cases/USE_CASE_3/README.md](./use-cases/USE_CASE_3/README.md) for details and access instructions.

---

## Additional Documentation

- [USE_CASES.md](./USE_CASES.md) - Main document with all use cases
- [AUTHENTICATION_GLOSSARY.md](./AUTHENTICATION_GLOSSARY.md) - Glossary of authentication and authorization terms

## Requirements

- Docker and Docker Compose
- Modern web browser
- (Optional) Google OAuth 2.0 credentials to test social login

## Notes

- Each use case is independent and can be run separately
- Use cases share concepts and patterns, but are organized to facilitate development and maintenance
- It is recommended to review the documentation of each use case before running it
