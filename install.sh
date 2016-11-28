sudo apt-get -y install git wget dh-autoreconf libssl-dev libtool libc6-dev
git clone https://github.com/ashishkurian/ovs.git
cd ovs
sudo ./boot.sh
sudo ./configure --with-linux=/lib/modules/`uname -r`/build
sudo make
sudo make install
sudo cp datapath/linux/openvswitch.ko /lib/modules/`uname -r`/kernel/net/openvswitch/openvswitch.ko
sudo make modules_install
/sbin/modprobe openvswitch
/sbin/lsmod
sudo mkdir -p /usr/local/etc/openvswitch
sudo ovsdb-tool create /usr/local/etc/openvswitch/conf.db vswitchd/vswitch.ovsschema
sudo mkdir -p /usr/local/var/run/openvswitch
sudo ovsdb-server --remote=punix:/usr/local/var/run/openvswitch/db.sock --remote=db:Open_vSwitch,Open_vSwitch,manager_options --private-key=db:Open_vSwitch,SSL,private_key --certificate=db:Open_vSwitch,SSL,certificate --bootstrap-ca-cert=db:Open_vSwitch,SSL,ca_cert --pidfile --detach
sudo ovs-vsctl --no-wait init
sudo ovs-vswitchd --pidfile --detach
