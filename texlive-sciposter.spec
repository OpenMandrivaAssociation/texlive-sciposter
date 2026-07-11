%global tl_name sciposter
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.18
Release:	%{tl_revision}.1
Summary:	Make posters of ISO A3 size and larger
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sciposter
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sciposter.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sciposter.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This collection of files contains LaTeX packages for posters of ISO A3
size and larger (ISO A0 is the default size). American paper sizes and
custom paper are supported. In particular, sciposter.cls defines a
document class which allows cutting and pasting most of an article to a
poster without any editing (save reducing the size) -- see the manual.
Sciposter does work for LaTeX, not just pdfLaTeX. However, xdvi produces
strange results, though a recent version of dvips does create good ps-
files from the dvi files. Also note that logos must either be put in the
current working directory or in the directories of your LaTeX
distribution. For some reason graphicspath settings are ignored.

