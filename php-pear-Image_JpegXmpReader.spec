%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Image_JpegXmpReader
Summary:	%{_pearname} - Read Photoshop-style XMP metadata from JPEG files
Summary(pl.UTF-8):	%{_pearname} - odczyt metadanych XMP z plików JPEG
Name:		php-pear-%{_pearname}
Version:	0.5.1
Release:	2
License:	MIT License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	098dc489c341f42f4c8c1274d295a094
URL:		http://pear.php.net/package/Image_JpegXmpReader/
BuildRequires:	php-pear-PEAR
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear-Image_JpegMarkerReader
Requires:	php-pear-PEAR >= 1.4.0
Requires:	php-pear-XML_Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package fetches Photoshop-style XMP metadata from JPEG files.
Convenience functions are provided to fetch the title, creator,
subject and description fields, other fields can be fetched by name,
and the parsed XML can be accessed directly. It is a useful tool for
accessing JPEGs edited with newer tools that do not provide EXIF
metadata and/or provide additional information as XMP.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten umożliwa pobranie metadanych XMP (w formacie Photoshopa) z
plików JPEG. Za pomocą wygodnych w użyciu funkcji możliwe jest
pobranie pól takich jak tytuł, autor, temat czy opis, poprzez nazwę
lub bezpośrednio przez XML. Jest to wygodne narzędzie do obróbki
plików JPEG edytowanych za pomocą narzędzi nie zapisujących informacji
w metadanych EXIF i/lub dostarczających dodatkowe informacje jako XMP.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Image/JpegXmpReader.php
