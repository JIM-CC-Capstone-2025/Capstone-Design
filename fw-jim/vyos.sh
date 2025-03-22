set interfaces ethernet eth0 address [figure out later]
set interfaces ethernet eth0 description 'WAN'
set interfaces ethernet eth1 address '192.168.1.1/24'
set interfaces ethernet eth1 description 'LAN'
set interfaces ethernet eth2 address '192.168.2.1/24'
set interfaces ethernet eth2 description 'DMZ'
set zone-policy zone WAN interface eth0
set zone-policy zone LAN interface eth1
set zone-policy zone DMZ interface eth2
