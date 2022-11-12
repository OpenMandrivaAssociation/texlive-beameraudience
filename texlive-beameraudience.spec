Name:		texlive-beameraudience
Version:	23427
Release:	1
Summary:	Assembling beamer frames according to audience
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/beameraudience
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beameraudience.r23427.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beameraudience.doc.r23427.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Beamer Audience package provides macros to easily assemble
frames according to different audiences. It enables to pick up
the frames for a specific audience while leaving their order
according to a logical structure in the LaTeX source.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/beameraudience/beameraudience.sty
%doc %{_texmfdistdir}/doc/latex/beameraudience/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
