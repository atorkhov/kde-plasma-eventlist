%global applet_name events

Name:           kde-plasma-eventlist
Version:        0.5.95
Release:        1%{?dist}
Summary:        Eventlist Plasmoid

Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://kde-look.org/content/show.php/Eventlist?content=107779
#Source0:        http://kde-look.org/CONTENT/content-files/107779-plasmoid-eventlist-0.5.95.tar.bz2
Source0:        plasmoid-eventlist-0.5.95.tar.bz2

BuildRequires:  cmake gettext kdebase-workspace-devel kdepimlibs-devel akonadi-devel kdelibs-devel

%description
This is a plasmoid to show the events from Akonadi resources (KOrganizer, Birthdays etc.).


%prep
%setup -q -n plasmoid-eventlist-%{version}


%build
%{cmake_kde4}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang plasma_applet_%{applet_name}


%files -f plasma_applet_%{applet_name}.lang
%doc AUTHORS Changelog COPYING README TODO
%{_libdir}/kde4/plasma_applet_%{applet_name}.so
%{_datadir}/kde4/services/plasma-applet-%{applet_name}.desktop


%changelog
* Sun Jan 15 2012 Alexey Torkhov <atorkhov@gmail.com> - 0.5.95-1..R
- Initial package.

