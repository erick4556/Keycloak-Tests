# Use Cases - Keycloak for Identification and Authentication

This document describes the use cases identified for implementing Keycloak in the identification and authentication system.

## General Status

| Use Case | Description | Status | Folder |
|----------|-------------|--------|--------|
| USE_CASE_1 | Single Sign-On (SSO) in corporate and citizen applications | ✅ Done | `use-cases/USE_CASE_1/` |
| USE_CASE_2 | Machine authentication - WEB services - Secrets vault | ✅ Done | `use-cases/USE_CASE_2/` |
| USE_CASE_3 | Citizen identification (natural + legal + European persons) | ✅ Done | `use-cases/USE_CASE_3/` |

---

## USE_CASE_1: Single Sign-On (SSO) in Corporate and Citizen Applications

### Description
Implementation of Single Sign-On (SSO) for corporate applications and also for citizens. The risks of an employee acting as a citizen in the same session must be evaluated.

### Objectives
- Allow corporate users to access multiple applications with a single authentication
- Allow citizens to access public services with a single authentication
- Manage the risk of an employee acting as a citizen in the same session
- Implement separation of authentication contexts when necessary

### Security Considerations
- **Identified risk**: An employee can act as a citizen in the same session
- **Mitigation**: Evaluate the need to separate sessions or implement additional authorization controls
- **ENS Level**: To be determined according to usage context

### Current Implementation
- ✅ Unified realm (`unified-realm`) containing corporate and citizen applications
- ✅ Users can have both employee and citizen roles simultaneously
- ✅ Multiple client applications configured in the same realm
- ✅ Integration with Google as Identity Provider
- ✅ SSO working between all applications (corporate and citizen) with a single authentication
- ⚠️ Security risks documented for dual sessions (employee/citizen)

### Next Steps
- [ ] Document strategy for managing dual sessions (employee/citizen)
- [ ] Implement session policies to prevent conflicts
- [ ] Define required security levels
- [ ] Create test cases to validate behavior

**Folder**: `use-cases/USE_CASE_1/`

---

## USE_CASE_2: Machine Authentication - WEB Services - Secrets Vault

### Description
Authentication of machines and WEB services, including integration with secrets vault (currently Passbolt). It should be evaluated whether authentication will be by certificate, by username/password, etc. (currently auth.properties).

### Objectives
- Implement authentication for services and machines (Service-to-Service)
- Integrate with secrets management system (Passbolt)
- Define authentication method (certificate, username/password, tokens)
- Replace or complement current system (auth.properties)

### Technical Considerations
- **Current method**: auth.properties
- **Options to evaluate**:
  - Certificate authentication
  - Username/password
  - Client Credentials Grant (OAuth 2.0)
  - mTLS (Mutual TLS)
- **Integration**: Secrets vault (Passbolt)

### Current Implementation
- ✅ Realm `machine-realm` with clients for service-to-service authentication
- ✅ `app-x` consuming secrets from Passbolt real with a GPG-authenticated service account
- ✅ `app-x` obtaining token from Keycloak via Client Credentials Grant
- ✅ `app-z` protected API validating tokens with Keycloak introspection

### Status
✅ Done

**Folder**: `use-cases/USE_CASE_2/`

---

## USE_CASE_3: Citizen Identification

### Description
Citizen identification for natural persons, legal persons, and European persons. Currently providers are electronic certificate and Cl@ve system. The possibility of username/password should be evaluated (careful with ENS level!).

### Objectives
- Integrate multiple identity providers:
  - Electronic certificate
  - Cl@ve system
  - Username/password (to be evaluated according to ENS level)
- Support for:
  - Natural persons
  - Legal persons
  - European persons

### Security Considerations
- **ENS Level**: Critical - must comply with National Security Scheme requirements
- **Current providers**:
  - Electronic certificate
  - Cl@ve system
- **New provider to evaluate**: Username/password (requires ENS level evaluation)

### External Repository

This use case is implemented and maintained in an external repository:

> 🔗 **[https://github.com/manabcodes/Keycloak-Tests-7](https://github.com/manabcodes/Keycloak-Tests-7)**

See [use-cases/USE_CASE_3/README.md](./use-cases/USE_CASE_3/README.md) for local access instructions.

### Status
✅ Done

**Folder**: `use-cases/USE_CASE_3/`

---

## General Notes

- All use cases must consider compliance with the National Security Scheme (ENS)
- Implementation must be scalable and maintainable
- Each use case must be documented with practical examples
- Tests must be created to validate each implementation
