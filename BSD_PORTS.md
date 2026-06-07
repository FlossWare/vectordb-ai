# BSD Ports Support

FlossWare AI projects support BSD systems via the Ports system.

## BSD Packaging Overview

Unlike Linux (RPM/DEB), BSDs use **Ports**:
- **FreeBSD**: `/usr/ports/` (FreeBSD Ports Collection)
- **OpenBSD**: `/usr/ports/` (OpenBSD Ports Tree)
- **NetBSD**: `/usr/pkgsrc/` (pkgsrc - portable across all BSDs + Solaris)

---

## FreeBSD

### Package Structure

```
/usr/ports/devel/py-vectordb-ai/
├── Makefile              # Port configuration
├── distinfo              # Checksums
├── pkg-descr             # Description
└── pkg-plist             # File list
```

### Example Makefile

```makefile
PORTNAME=       vectordb-ai
DISTVERSIONPREFIX=      v
DISTVERSION=    0.2
CATEGORIES=     devel python
PKGNAMEPREFIX=  ${PYTHON_PKGNAMEPREFIX}

MAINTAINER=     noreply@flossware.org
COMMENT=        Universal vector database adapter for AI applications
WWW=            https://github.com/FlossWare/vectordb-ai

LICENSE=        GPLv3
LICENSE_FILE=   ${WRKSRC}/LICENSE

USES=           python
USE_PYTHON=     autoplist distutils

USE_GITHUB=     yes
GH_ACCOUNT=     FlossWare

.include <bsd.port.mk>
```

### Installation

```bash
# From ports
cd /usr/ports/devel/py-vectordb-ai
make install clean

# From packages (pre-built)
pkg install py39-vectordb-ai
```

---

## OpenBSD

### Package Structure

```
/usr/ports/devel/py-vectordb-ai/
├── Makefile              # Port configuration
├── distinfo              # Checksums
└── pkg/
    ├── DESCR             # Description
    └── PLIST             # File list
```

### Example Makefile

```makefile
COMMENT=        universal vector database adapter for AI applications

MODPY_EGG_VERSION=      0.2
DISTNAME=       vectordb-ai-${MODPY_EGG_VERSION}
PKGNAME=        py-${DISTNAME}

CATEGORIES=     devel

HOMEPAGE=       https://github.com/FlossWare/vectordb-ai

MAINTAINER=     FlossWare <noreply@flossware.org>

# GPLv3
PERMIT_PACKAGE= Yes

MODULES=        lang/python

MODPY_PI=       Yes
MODPY_SETUPTOOLS=       Yes

.include <bsd.port.mk>
```

### Installation

```bash
# From ports
cd /usr/ports/devel/py-vectordb-ai
make install

# From packages
pkg_add py3-vectordb-ai
```

---

## NetBSD (pkgsrc)

### Package Structure

```
/usr/pkgsrc/devel/py-vectordb-ai/
├── Makefile              # Port configuration
├── distinfo              # Checksums
├── DESCR                 # Description
└── PLIST                 # File list
```

### Example Makefile

```makefile
DISTNAME=       vectordb-ai-0.2
PKGNAME=        ${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=     devel python
MASTER_SITES=   ${MASTER_SITE_GITHUB:=FlossWare/}

MAINTAINER=     pkgsrc-users@NetBSD.org
HOMEPAGE=       https://github.com/FlossWare/vectordb-ai
COMMENT=        Universal vector database adapter for AI applications
LICENSE=        gnu-gpl-v3

USE_LANGUAGES=  # none

PYTHON_VERSIONS_INCOMPATIBLE=   27

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
```

### Installation

```bash
# From pkgsrc
cd /usr/pkgsrc/devel/py-vectordb-ai
make install

# From binary packages
pkgin install py39-vectordb-ai
```

---

## Cross-Platform pkgsrc

**pkgsrc** is portable and works on:
- ✅ NetBSD (native)
- ✅ FreeBSD
- ✅ OpenBSD
- ✅ DragonFly BSD
- ✅ macOS
- ✅ Linux
- ✅ Solaris/illumos

### Installation (any OS with pkgsrc)

```bash
cd /usr/pkgsrc/devel/py-vectordb-ai
bmake install
```

---

## Creating BSD Ports

To submit FlossWare AI to BSD ports:

### FreeBSD
1. Create port in `/usr/ports/devel/py-vectordb-ai/`
2. Test with `portlint`
3. Submit PR: https://bugs.freebsd.org/bugzilla/

### OpenBSD
1. Create port in `/usr/ports/devel/py-vectordb-ai/`
2. Test with `make port-lib-depends-check`
3. Submit to ports@openbsd.org

### NetBSD (pkgsrc)
1. Create package in `/usr/pkgsrc/devel/py-vectordb-ai/`
2. Test with `pkglint`
3. Submit PR: https://github.com/NetBSD/pkgsrc

---

## Package Names by BSD

| BSD | Package Name | Binary Package Manager |
|-----|-------------|------------------------|
| **FreeBSD** | `py39-vectordb-ai` | `pkg` |
| **OpenBSD** | `py3-vectordb-ai` | `pkg_add` |
| **NetBSD** | `py39-vectordb-ai` | `pkgin` |
| **DragonFly** | `py39-vectordb-ai` | `pkg` |

---

## Current Status

| Project | FreeBSD Port | OpenBSD Port | pkgsrc | Status |
|---------|--------------|--------------|---------|--------|
| vectordb-ai | 🔄 Planned | 🔄 Planned | 🔄 Planned | Preparing |
| semantic-search-ai | 🔄 Planned | 🔄 Planned | 🔄 Planned | Preparing |
| knowledge-ai | 🔄 Planned | 🔄 Planned | 🔄 Planned | Preparing |
| consensus-ai | 🔄 Planned | 🔄 Planned | 🔄 Planned | Preparing |

---

## Why BSD Ports Matter

✅ **Official distribution** - In OS repos  
✅ **Trusted** - Maintained by BSD committers  
✅ **Security** - Audited by BSD security teams  
✅ **Integration** - Works with BSD package system  
✅ **pkgsrc portability** - Works on all BSDs + Solaris  

---

## Fallback: pip on BSD

While ports are being prepared, install via pip:

```bash
# FreeBSD
pkg install python39 py39-pip
pip install vectordb-ai

# OpenBSD
pkg_add python3 py3-pip
pip install vectordb-ai

# NetBSD
pkgin install python39 py39-pip
pip install vectordb-ai
```

---

## Contributing

Want to help create BSD ports? See [CONTRIBUTING.md](CONTRIBUTING.md)

**Contact:** noreply@flossware.org
