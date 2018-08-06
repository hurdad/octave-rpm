Name:           octave
Version:        %{VERSION}
Release:        1%{?dist}
Summary:        A high-level language for numerical computations
Group:          Applications/Engineering
License:        GPLv3+
URL:            http://www.octave.org
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Provides:       octave(api) = %{octave_api}
Provides:       bundled(gnulib)

BuildRequires:  arpack-devel
BuildRequires:  atlas-devel 
BuildRequires:  bison
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  flex
BuildRequires:  fltk-devel
BuildRequires:  ftgl-devel
BuildRequires:  gcc-gfortran
BuildRequires:  ghostscript
BuildRequires:  gl2ps-devel
BuildRequires:  glpk-devel
BuildRequires:  gnuplot
BuildRequires:  gperf
BuildRequires:  GraphicsMagick-c++-devel
BuildRequires:  hdf5-devel
BuildRequires:  java-devel
BuildRequires:  less
BuildRequires:  libX11-devel
BuildRequires:  llvm-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ncurses-devel
BuildRequires:  pcre-devel
BuildRequires:  qhull-devel
BuildRequires:  qrupdate-devel
BuildRequires:  qscintilla-devel
BuildRequires:  readline-devel
BuildRequires:  suitesparse-devel
BuildRequires:  tex(dvips)
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  zlib-devel

Requires:        epstool gnuplot gnuplot-common less info texinfo 
Requires:        hdf5 = %{_hdf5_version}
Requires:        java-headless
Requires(post):  info
Requires(preun): info

%description
GNU Octave is a high-level language, primarily intended for numerical
computations. It provides a convenient command line interface for
solving linear and nonlinear problems numerically, and for performing
other numerical experiments using a language that is mostly compatible
with Matlab. It may also be used as a batch-oriented language. Octave
has extensive tools for solving common numerical linear algebra
problems, finding the roots of nonlinear equations, integrating
ordinary functions, manipulating polynomials, and integrating ordinary
differential and differential-algebraic equations. It is easily
extensible and customizable via user-defined functions written in
Octave's own language, or using dynamically loaded modules written in
C++, C, Fortran, or other languages.

%package devel
Summary:        Development headers and files for Octave
Group:          Development/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       readline-devel fftw-devel hdf5-devel zlib-devel
Requires:       atlas-devel gcc-c++ gcc-gfortran

%description devel
The octave-devel package contains files needed for developing
applications which use GNU Octave.

%prep
%setup -n %{name}-%{version}

%build
%configure --enable-shared \
			 --disable-static \
			 --enable-float-truncate \
			 --with-qrupdate \
			 --with-amd \
			 --with-umfpack \
			 --with-colamd \
			 --with-ccolamd \
			 --with-cholmod \
			 --with-cxsparse \
			 --disable-jit
make %{?_smp_mflags} 

%install
make install DESTDIR=%{buildroot}

%check
make check

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%doc AUTHORS BUGS ChangeLog NEWS README
%license COPYING
%{_bindir}/octave*
%{_libdir}/octave/
%{_libexecdir}/octave/
%{_datarootdir}/octave/
%{_datarootdir}/applications/org.octave.Octave.desktop
%{_datarootdir}/icons/
%{_datarootdir}/metainfo/org.octave.Octave.appdata.xml

%files devel
%{_bindir}/mkoctfile
%{_bindir}/mkoctfile-%{version}
%{_includedir}/octave-%{version}/

%changelog
