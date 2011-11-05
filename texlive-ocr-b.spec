# revision 20852
# category Package
# catalog-ctan /fonts/ocr-b
# catalog-date 2010-12-24 15:25:32 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-ocr-b
Version:	20101224
Release:	1
Summary:	Fonts for OCR-B
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ocr-b
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-b.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocr-b.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3

%description
MetaFont programs for OCR-B at several sizes.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}