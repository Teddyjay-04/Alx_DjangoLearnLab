# Permissions & Groups Setup

## Custom Permissions
- `can_view` → Can view books
- `can_create` → Can create books
- `can_edit` → Can edit books
- `can_delete` → Can delete books

## Groups
- **Editors** → Can create and edit books
- **Viewers** → Can only view books
- **Admins** → Full permissions

## Usage
- Permissions enforced in views using `@permission_required()`
- Groups assigned automatically via Django signals

# Django HTTPS Security Configuration

## Implemented Security Settings:
1. **HTTPS Enforcement**  
   - `SECURE_SSL_REDIRECT = True`: Redirects all HTTP traffic to HTTPS.
   - `SECURE_HSTS_SECONDS = 31536000`: Enforces HTTPS for one year.
   - `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS to all subdomains.
   - `SECURE_HSTS_PRELOAD = True`: Allows browser preloading.

2. **Secure Cookies**  
   - `SESSION_COOKIE_SECURE = True`: Prevents session hijacking.
   - `CSRF_COOKIE_SECURE = True`: Protects CSRF cookies.

3. **Security Headers**  
   - `X_FRAME_OPTIONS = "DENY"`: Prevents clickjacking attacks.
   - `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME sniffing.
   - `SECURE_BROWSER_XSS_FILTER = True`: Enables browser’s XSS filtering.

## Deployment Setup:
- Use **Let's Encrypt** for free SSL certificates:
- Modify **NGINX/Apache** configuration to enforce HTTPS.

## Testing:
1. Visit `https://yourdomain.com/` to verify HTTPS redirection.
2. Check browser console for security warnings.
3. Run:
