Name:		texlive-ocr-b
Version:	20852
Release:	2
Summary:	Fonts for OCR-B
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ocr-b
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-b.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-b.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
MetaFont programs for OCR-B at several sizes.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/ocr-b/ocrb10.mf
%{_texmfdistdir}/fonts/source/public/ocr-b/ocrb10e.mf
%{_texmfdistdir}/fonts/source/public/ocr-b/ocrb10f.mf
%{_texmfdistdir}/fonts/source/public/ocr-b/ocrb10g.mf
%{_texmfdistdir}/fonts/source/public/ocr-b/ocrb10l.mf
%{_texmfdistdir}/fonts/source/public/ocr-b/ocrb10s.mf
%{_texmfdistdir}/fonts/source/public/ocr-b/ocrb10x.mf
%{_texmfdistdir}/fonts/source/public/ocr-b/ocrb5.mf
%{_texmfdistdir}/fonts/source/public/ocr-b/ocrb6.mf
%{_texmfdistdir}/fonts/source/public/ocr-b/ocrb7.mf
%{_texmfdistdir}/fonts/source/public/ocr-b/ocrb8.mf
%{_texmfdistdir}/fonts/source/public/ocr-b/ocrb9.mf
%{_texmfdistdir}/fonts/source/public/ocr-b/ocrbdef.mf
%{_texmfdistdir}/fonts/source/public/ocr-b/ocrbmac.mf
%{_texmfdistdir}/fonts/tfm/public/ocr-b/ocrb10.tfm
%{_texmfdistdir}/fonts/tfm/public/ocr-b/ocrb5.tfm
%{_texmfdistdir}/fonts/tfm/public/ocr-b/ocrb6.tfm
%{_texmfdistdir}/fonts/tfm/public/ocr-b/ocrb7.tfm
%{_texmfdistdir}/fonts/tfm/public/ocr-b/ocrb8.tfm
%{_texmfdistdir}/fonts/tfm/public/ocr-b/ocrb9.tfm
%doc %{_texmfdistdir}/doc/fonts/ocr-b/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
