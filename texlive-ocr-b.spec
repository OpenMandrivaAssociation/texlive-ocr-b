%global tl_name ocr-b
%global tl_revision 20852

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Fonts for OCR-B
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ocr-b
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-b.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-b.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Metafont source for OCR-B at several sizes.

