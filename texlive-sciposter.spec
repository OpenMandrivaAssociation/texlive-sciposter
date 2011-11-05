# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sciposter
# catalog-date 2007-02-26 21:24:31 +0100
# catalog-license lppl
# catalog-version 1.18
Name:		texlive-sciposter
Version:	1.18
Release:	1
Summary:	Make posters of ISO A3 size and larger
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sciposter
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sciposter.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sciposter.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This collection of files contains LaTeX packages for posters of
ISO A3 size and larger (ISO A0 is the default size). American
paper sizes and custom paper are supported. In particular,
sciposter.cls defines a document class which allows cutting and
pasting most of an article to a poster without any editing
(save reducing the size) -- see the manual. Sciposter does work
for LaTeX, not just pdfLaTeX. However, xdvi produces strange
results, though a recent version of dvips does create good ps-
files from the dvi files. Also note that logos must either be
put in the current working directory or in the directories of
your LaTeX distribution. For some reason graphicspath settings
are ignored.

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
%{_texmfdistdir}/tex/latex/sciposter/paperb0.cfg
%{_texmfdistdir}/tex/latex/sciposter/paperb1.cfg
%{_texmfdistdir}/tex/latex/sciposter/paperb2.cfg
%{_texmfdistdir}/tex/latex/sciposter/paperb3.cfg
%{_texmfdistdir}/tex/latex/sciposter/papercustom.cfg
%{_texmfdistdir}/tex/latex/sciposter/paperra0.cfg
%{_texmfdistdir}/tex/latex/sciposter/paperra1.cfg
%{_texmfdistdir}/tex/latex/sciposter/paperra2.cfg
%{_texmfdistdir}/tex/latex/sciposter/sciposter.cls
%doc %{_texmfdistdir}/doc/latex/sciposter/README
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/auto/sciposter-example.el
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks1.eps
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks1.pdf
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks1a.eps
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks1a.pdf
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks1mx.eps
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks1mx.pdf
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks1vx.eps
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks1vx.pdf
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks2.eps
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks2.pdf
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks2mx.eps
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks2mx.pdf
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3.eps
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3.pdf
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3mx.eps
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3mx.pdf
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3op.eps
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3op.pdf
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3openvx.eps
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3rec.eps
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3rec.pdf
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3vx.eps
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocks3vx.pdf
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocksopen3a.eps
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocksopen3a.pdf
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocksopen3vx.eps
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocksopen3vx.pdf
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocksopen3vy.eps
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/blocksopen3vy.pdf
%doc %{_texmfdistdir}/doc/latex/sciposter/sciposterexample/sciposter-example.tex
%doc %{_texmfdistdir}/doc/latex/sciposter/scipostermanual.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
