Name:		texlive-beameraudience
Version:	0.1
Release:	1
Summary:	Assembling beamer frames according to audience
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/beameraudience
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beameraudience.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beameraudience.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The Beamer Audience package provides macros to easily assemble
frames according to different audiences. It enables to pick up
the frames for a specific audience while leaving their order
according to a logical structure in the LaTeX source.

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
%{_texmfdistdir}/tex/latex/beameraudience/beameraudience.sty
%doc %{_texmfdistdir}/doc/latex/beameraudience/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
