%define name weechat
%define version 0.3.0
%define release %mkrel 1
%define Werror_cflags %nil
%define weegtk 0

%{?_without_gtk: %{expand: %%define weegkt 0}}
%{?_with_gtk: %{expand: %%define weegkt 1}}

Summary: Wee Enhanced Environment for Chat
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.weechat.org/files/src/%{name}-%{version}.tar.gz
Patch0:  weechat-0.3.0-cmake-paths.patch
Patch1:  weechat-0.3.0-cmake-pie.patch
License: GPL
Group: Networking/IRC
Url: http://www.weechat.org/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ncurses-devel
# next need for utf8 support
BuildRequires: ncursesw-devel
BuildRequires: perl-devel
# Ruby & Python are really needed for the build, tks lbd
BuildRequires: python-devel
BuildRequires: ruby-devel
Buildrequires: lua-devel
BuildRequires: aspell-devel
BuildRequires: gettext-devel
BuildRequires: libgnutls-devel
BuildRequires: libgtk+2-devel

%description
WeeChat (Wee Enhanced Environment for Chat) is a free IRC client, fast and
light, designed for many operating systems.
 
Main features are: 
  - multi-servers connection
  - many GUI (Graphical User Interface): Curses, Gtk and Qt 
  - small, fast and light
  - customizable and extensible with scripts
  - compliant with RFCs 1459, 2810, 2811, 2812, and 2813
  - multi-platform (Gnu/Linux, *BSD, Windows and other)
  - 100% GPL, free software

Install %name-gtk to have the gtk-gui.

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info


%files -f build/%name.lang
%defattr(-,root,root)
%_bindir/%name
%_bindir/%name-curses
%_mandir/man1/weechat*
%dir %_prefix/lib*/%name
%dir %_prefix/lib*/%name/plugins
%_prefix/lib*/%name/plugins/alias.so
%_prefix/lib*/%name/plugins/fifo.so
%_prefix/lib*/%name/plugins/irc.so
%_prefix/lib*/%name/plugins/logger.so
%_prefix/lib*/%name/plugins/xfer.so

#--------------------------------------------------------------------

%if %weegtk
%package gtk
Group: Networking/IRC
Summary: Wee Enhanced Environment for Chat (With GTK)
Requires: %name = %version

%description gtk
WeeChat (Wee Enhanced Environment for Chat) is a free IRC client, fast and
light, designed for many operating systems.
 
Main features are: 
  - multi-servers connection 
  - many GUI (Graphical User Interface): Curses, Gtk and Qt 
  - small, fast and light 
  - customizable and extensible with scripts 
  - compliant with RFCs 1459, 2810, 2811, 2812, and 2813 
  - multi-platform (Gnu/Linux, *BSD, Windows and other) 
  - 100% GPL, free software

This package contain %name-gtk

%files gtk
%defattr(-,root,root)
%_bindir/%name-gtk
%endif

#--------------------------------------------------------------------

%package perl
Group: Networking/IRC
Summary: Weechat perl plugins
Requires: %name = %version

%description perl
This package allow weechat to use perl scripts

%files perl
%defattr(-,root,root)
%_prefix/lib*/%name/plugins/*perl*

#--------------------------------------------------------------------

%package python
Group: Networking/IRC
Summary: Weechat python plugins
Requires: %name = %version

%description python
This package allow weechat to use python scripts

%files python
%defattr(-,root,root)
%_prefix/lib*/%name/plugins/*python*

#--------------------------------------------------------------------

%package tcl
Group: Networking/IRC
Summary: Weechat tcl plugins
Requires: %name = %version

%description tcl
This package allow weechat to use tcl scripts

%files tcl
%defattr(-,root,root)
%_prefix/lib*/%name/plugins/*tcl*

#--------------------------------------------------------------------

%package ruby
Group: Networking/IRC
Summary: Weechat ruby plugins
Requires: %name = %version

%description ruby
This package allow weechat to use ruby scripts

%files ruby
%defattr(-,root,root)
%_prefix/lib*/%name/plugins/*ruby*

#--------------------------------------------------------------------

%package lua
Group: Networking/IRC
Summary: Weechat lua plugins
Requires: %name = %version

%description lua
This package allow weechat to use lua scripts

%files lua
%defattr(-,root,root)
%_prefix/lib*/%name/plugins/*lua*

#--------------------------------------------------------------------

%package charset
Group: Networking/IRC
Summary: Weechat charset plugins
Requires: %name = %version

%description charset
This package allow weechat to use charset

%files charset
%defattr(-,root,root)
%_prefix/lib*/%name/plugins/*charset*

#--------------------------------------------------------------------

%package aspell
Group: Networking/IRC
Summary: Weechat aspell plugins
Requires: %name = %version

%description aspell
This package allow weechat to use aspell

%files aspell
%defattr(-,root,root)
%_prefix/lib*/%name/plugins/*aspell*

#--------------------------------------------------------------------

%package devel
Summary: Development files for weechat
Group: Development/Libraries
Requires: %{name} = %{version}-%{release} pkgconfig

%description devel
WeeChat (Wee Enhanced Environment for Chat) is a portable, fast, light and
extensible IRC client. Everything can be done with a keyboard.
It is customizable and extensible with scripts.

This package contains include files and pc file for weechat.

%files devel
%defattr(-,root,root)
%_includedir/weechat
%_libdir/pkgconfig/weechat.pc

#--------------------------------------------------------------------

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1

%build
%cmake \
%if %weegtk
    -DENABLE_GTK=ON
%else
    -DENABLE_GTK=OFF
%endif

%make

%install
rm -fr %buildroot
cd build
%makeinstall_std

(
cd %buildroot%_bindir
ln -s %name-curses %name
)

%find_lang %name

%clean
rm -rf %buildroot
