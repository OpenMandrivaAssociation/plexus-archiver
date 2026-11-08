Name:		plexus-archiver
Version:	4.15.0
Release:	1
Summary:	Plexus archiver component
Group:		Development/Java
License:	ASL 2.0
URL:		https://codehaus-plexus.github.io/plexus-archiver/
Source0:	https://github.com/codehaus-plexus/plexus-archiver/archive/refs/tags/plexus-archiver-%{version}.tar.gz
BuildArch:	noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildRequires:	plexus-pom >= 27
BuildRequires:	mvn(org.codehaus.plexus:plexus:pom::)
BuildRequires:	plexus-utils >= 3.6.2
BuildRequires:	plexus-io >= 3.8.1
BuildRequires:	apache-commons-io >= 1:2.22.0
BuildRequires:	mvn(commons-io:commons-io)
BuildRequires:	apache-commons-compress >= 1.28.0
BuildRequires:	mvn(org.apache.commons:commons-compress)
BuildRequires:	mvn(org.slf4j:slf4j-api)
BuildRequires:	xz-java >= 1.12
BuildRequires:	mvn(org.tukaani:xz)
BuildRequires:	javax.inject >= 1-2
BuildRequires:	mvn(javax.inject:javax.inject)
# provided scope: sources import javax.annotation, and Maven still resolves it
BuildRequires:	jsr-305 >= 3.0.2-3
BuildRequires:	mvn(com.google.code.findbugs:jsr305)
# 3.2.1 and 1.10 still provide these coordinates. The generated mvn()
# Requires are unversioned, so pin the packages that 4.15.0 compiles against.
Requires:	plexus-utils >= 3.6.2
Requires:	apache-commons-compress >= 1.28.0
# jakarta-inject provides the same unversioned mvn(javax.inject:javax.inject).
Requires:	javax.inject >= 1-2
Requires:	xz-java >= 1.12
BuildSystem:	maven
BuildOption(install):	--file-name %{name}

%description
Creates and extracts zip, tar, jar, and related archives. 4.15.0
builds against Plexus Utils 3.6.2, Plexus IO 3.8.1, Commons Compress
1.28.0, and Commons IO 2.22.0. Snappy is the framed format from
Commons Compress. Zstandard is left out, matching Commons Compress,
because zstd-jni is a prebuilt native library. An entry whose
canonical path leaves the destination directory is rejected. An
existing file is replaced when overwrite is set, and also when the
file on disk is older than the entry. Reproducible builds force uid
and gid 0, name them root, sort entry names, and apply umask 022. A
file set can follow symbolic links. When the file system refuses a
symbolic link, the default is to copy the link target instead; a
target outside the destination, a missing target, and a link cycle
are skipped. The manifest automatic module name is
org.codehaus.plexus.archiver.

%prep
%autosetup -n plexus-archiver-plexus-archiver-%{version}
# Zstandard needs com.github.luben:zstd-jni, a prebuilt native library.
# Commons Compress in this distribution does not ship that package.
python - <<'PY'
import shutil
from pathlib import Path

def sub(path, old, new):
    file = Path(path)
    text = file.read_text()
    if old not in text:
        raise SystemExit("missing snippet in " + str(path))
    file.write_text(text.replace(old, new, 1))

for rel in (
    "src/main/java/org/codehaus/plexus/archiver/tar/PlexusIoTZstdFileResourceCollection.java",
    "src/main/java/org/codehaus/plexus/archiver/tar/PlexusIoTarZstdFileResourceCollection.java",
    "src/main/java/org/codehaus/plexus/archiver/tar/TZstdArchiver.java",
    "src/main/java/org/codehaus/plexus/archiver/tar/TZstdUnArchiver.java",
    "src/main/java/org/codehaus/plexus/archiver/tar/TarZstdArchiver.java",
    "src/main/java/org/codehaus/plexus/archiver/tar/TarZstdUnArchiver.java",
    "src/main/java/org/codehaus/plexus/archiver/tar/ZstdTarFile.java",
):
    path = Path(rel)
    if not path.is_file():
        raise SystemExit("missing " + rel)
    path.unlink()
zdir = Path("src/main/java/org/codehaus/plexus/archiver/zstd")
if not zdir.is_dir():
    raise SystemExit("missing zstd dir")
shutil.rmtree(zdir)
sub(
    "src/main/java/org/codehaus/plexus/archiver/tar/TarArchiver.java",
    "import org.apache.commons.compress.compressors.zstandard.ZstdCompressorOutputStream;\n",
    "",
)
sub(
    "src/main/java/org/codehaus/plexus/archiver/tar/TarArchiver.java",
    "        xz,\n        zstd\n",
    "        xz\n",
)
sub(
    "src/main/java/org/codehaus/plexus/archiver/tar/TarArchiver.java",
    "        } else if (TarCompressionMethod.xz.equals(tarCompressionMethod)) {\n"
    "            return new XZCompressorOutputStream(bufferedOutputStream(ostream));\n"
    "        } else if (TarCompressionMethod.zstd.equals(tarCompressionMethod)) {\n"
    "            return new ZstdCompressorOutputStream(bufferedOutputStream(ostream));\n"
    "        }\n",
    "        } else if (TarCompressionMethod.xz.equals(tarCompressionMethod)) {\n"
    "            return new XZCompressorOutputStream(bufferedOutputStream(ostream));\n"
    "        }\n",
)
sub(
    "src/main/java/org/codehaus/plexus/archiver/tar/TarUnArchiver.java",
    "import org.apache.commons.compress.compressors.zstandard.ZstdCompressorInputStream;\n",
    "",
)
sub(
    "src/main/java/org/codehaus/plexus/archiver/tar/TarUnArchiver.java",
    "        } else if (compression == UntarCompressionMethod.XZ) {\n"
    "            return new XZCompressorInputStream(istream);\n"
    "        } else if (compression == UntarCompressionMethod.ZSTD) {\n"
    "            return new ZstdCompressorInputStream(istream);\n"
    "        }\n",
    "        } else if (compression == UntarCompressionMethod.XZ) {\n"
    "            return new XZCompressorInputStream(istream);\n"
    "        }\n",
)
sub(
    "src/main/java/org/codehaus/plexus/archiver/tar/TarUnArchiver.java",
    '        XZ("xz"),\n        ZSTD("zstd");\n',
    '        XZ("xz");\n',
)
pom = Path("pom.xml")
text = pom.read_text()
old = (
    "    <dependency>\n"
    "      <groupId>com.github.luben</groupId>\n"
    "      <artifactId>zstd-jni</artifactId>\n"
    "      <version>1.5.7-16</version>\n"
    "      <scope>runtime</scope>\n"
    "    </dependency>\n"
)
if old not in text:
    raise SystemExit("pom zstd dependency missing")
pom.write_text(text.replace(old, "", 1))
PY
# Eclipse Sisu reads this index. ArchiverManager and the format
# handlers are @Named, and nothing classpath-scans them.
python - <<'PY'
import re
from pathlib import Path
root = Path("src/main/java")
names = []
for path in sorted(root.rglob("*.java")):
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"\b(?:class|interface|enum)\s+([A-Za-z0-9_]+)", text)
    if not match:
        continue
    if "@Named" not in text[:match.start()]:
        continue
    pkg = re.search(r"(?m)^package\s+([A-Za-z0-9_.]+)\s*;", text)
    if not pkg:
        continue
    names.append(pkg.group(1) + "." + match.group(1))
if names:
    dest = Path("src/main/resources/META-INF/sisu")
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "javax.inject.Named").write_text("\n".join(names) + "\n", encoding="utf-8")
PY

%files -f .mfiles
%doc LICENSE README.md ReleaseNotes.md
