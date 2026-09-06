For CI-builds, the recipies are available on the internal swift artifactory server.

To update these recipes from conancenter:

```bash
conan download --only-recipe pkgconf/2.1.0 -r conancenter
conan chace path pkgconf/2.1.0 <-- for reviewing recipe
conan upload "pkgconf/2.1.0" --remote own --only-recipe
```
