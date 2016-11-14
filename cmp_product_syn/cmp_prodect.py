#-*-coding:utf-8-*-
base_file = "D:/SKS_product/Testcase/主线/AP/WIA3200-80"

cmp_file = [
            "D:/SKS_product/Testcase/主线/AP/WOA5200-80P", 
            "D:/SKS_product/Testcase/主线/AP/WOA5600-60A", 
            "D:/SKS_product/Testcase/主线/AP/WIA3200-80S",
            "D:/SKS_product/Testcase/主线/AP/WIM1200-20"
           ]
           
#exclude_file = [r"D:\10.linlei_tool\cmp_product_syn\data\80p.txt", r"D:\10.linlei_tool\cmp_product_syn\data\60a.txt", r"D:\10.linlei_tool\cmp_product_syn\data\80s.txt"]
result_file = [
               r"D:\10.linlei_tool\cmp_product_syn\80p.txt", 
               r"D:\10.linlei_tool\cmp_product_syn\60a.txt", 
               r"D:\10.linlei_tool\cmp_product_syn\80s.txt",
               r"D:\10.linlei_tool\cmp_product_syn\sonoma.txt",
              ]

exclude_spc_file = ["__init__.txt", "comm_var.txt", "comm_proc.txt"]
exclude_suffix = [".pem"]

exclude_file = [
                #******************************************80p******************************************
                [
                 #不支持的功能
                 "wds*", "802.11n_ac*",
                 #业务问题
                 "AP_VLAN_0030", "Restore_Factory_Default_0030", "NAT-interface_0060", "NAT-interface_0270",
                 #5G
                 "Broadcast_Suppression_0180", "Broadcast_Suppression_0190", "Broadcast_Suppression_0360", "Broadcast_Suppression_0370", 
                 "Broadcast_Suppression_0380", "Broadcast_Suppression_0430", "Broadcast_Suppression_0470", "Broadcast_Suppression_0480",
                 "Broadcast_Suppression_0510", "Broadcast_Suppression_0520",
                 "MAC_ACL_0180", "MAC_ACL_0210", "MAC_ACL_0220",
                 "Bandwidth_Control_0250", "Bandwidth_Control_0260", "Bandwidth_Control_0270", "Bandwidth_Control_0310", "Bandwidth_Control_0320",
                 "Bandwidth_Control_0330", "Bandwidth_Control_0370", "Bandwidth_Control_0380", "Bandwidth_Control_0390", "Bandwidth_Control_0590",
                 "Bandwidth_Control_0570", "Bandwidth_Control_0580", "Bandwidth_Control_0630", "Bandwidth_Control_0640", "Bandwidth_Control_0650",
                 "Bandwidth_Control_0690", "Bandwidth_Control_0700", "Bandwidth_Control_0710", "Bandwidth_Control_0750", "Bandwidth_Control_0760",
                 "Bandwidth_Control_0770", "Bandwidth_Control_0810", "Bandwidth_Control_0820", "Bandwidth_Control_0830", "Bandwidth_Control_0840",
                 "Bandwidth_Control_0890", "Bandwidth_Control_0900", "Bandwidth_Control_0910", "Bandwidth_Control_0950", "Bandwidth_Control_0960",
                 "Bandwidth_Control_0970", "Bandwidth_Control_1010", "Bandwidth_Control_1020", "Bandwidth_Control_1030", "Bandwidth_Control_1070",
                 "Bandwidth_Control_1080", "Bandwidth_Control_1090", "Bandwidth_Control_1100", "Bandwidth_Control_1150", "Bandwidth_Control_1160",
                 "Bandwidth_Control_1170", "Bandwidth_Control_1180", "Bandwidth_Control_1270", "Bandwidth_Control_1280", "Bandwidth_Control_1300",
                 "Bandwidth_Control_1870", "Bandwidth_Control_1880", "Bandwidth_Control_1900",
                 "802.11a_b_g_n_0040", "802.11a_b_g_n_0050", "802.11a_b_g_n_0060", "802.11a_b_g_n_0120", "802.11a_b_g_n_0150", "802.11a_b_g_n_0200",
                 "802.11a_b_g_n_0210", "802.11a_b_g_n_0220", "802.11a_b_g_n_0230", "802.11a_b_g_n_0240", "802.11a_b_g_n_0270", "802.11a_b_g_n_0290",
                 "802.11a_b_g_n_0340", "802.11a_b_g_n_0360", "802.11a_b_g_n_0380", "802.11a_b_g_n_0250"
                 "location_0110",
                 "定时关断射频_0110", "定时关断射频_0140", "定时关断射频_0160", "定时关断射频_0170", "定时关断射频_0210",
                 "定时删除SSID_0020", "定时删除SSID_0040", "定时删除SSID_0060", "定时删除SSID_0010"
                 "无线接口管理_0040",  "无线接口管理_0310", "无线接口管理_0380", "无线接口管理_0420",
                 "最大用户数限制_0040", "最大用户数限制_0050", "最大用户数限制_0060",
                 "频点设置0020", "频点设置0050",
                ], 
                #******************************************80p******************************************
                #******************************************60A******************************************
                [
                 #不支持的功能
                 "802.11n_ac*",
                 #业务问题
                 "AP_VLAN_0030", "Restore_Factory_Default_0030",
                 #5G
                 "Broadcast_Suppression_0180", "Broadcast_Suppression_0190", "Broadcast_Suppression_0360", "Broadcast_Suppression_0370", 
                 "Broadcast_Suppression_0380", "Broadcast_Suppression_0430", "Broadcast_Suppression_0470", "Broadcast_Suppression_0480",
                 "Broadcast_Suppression_0510", "Broadcast_Suppression_0520",
                 "MAC_ACL_0180", "MAC_ACL_0210", "MAC_ACL_0220",
                 "Bandwidth_Control_0250", "Bandwidth_Control_0260", "Bandwidth_Control_0270", "Bandwidth_Control_0310", "Bandwidth_Control_0320",
                 "Bandwidth_Control_0330", "Bandwidth_Control_0370", "Bandwidth_Control_0380", "Bandwidth_Control_0390", "Bandwidth_Control_0590",
                 "Bandwidth_Control_0570", "Bandwidth_Control_0580", "Bandwidth_Control_0630", "Bandwidth_Control_0640", "Bandwidth_Control_0650",
                 "Bandwidth_Control_0690", "Bandwidth_Control_0700", "Bandwidth_Control_0710", "Bandwidth_Control_0750", "Bandwidth_Control_0760",
                 "Bandwidth_Control_0770", "Bandwidth_Control_0810", "Bandwidth_Control_0820", "Bandwidth_Control_0830", "Bandwidth_Control_0840",
                 "Bandwidth_Control_0890", "Bandwidth_Control_0900", "Bandwidth_Control_0910", "Bandwidth_Control_0950", "Bandwidth_Control_0960",
                 "Bandwidth_Control_0970", "Bandwidth_Control_1010", "Bandwidth_Control_1020", "Bandwidth_Control_1030", "Bandwidth_Control_1070",
                 "Bandwidth_Control_1080", "Bandwidth_Control_1090", "Bandwidth_Control_1100", "Bandwidth_Control_1150", "Bandwidth_Control_1160",
                 "Bandwidth_Control_1170", "Bandwidth_Control_1180", "Bandwidth_Control_1270", "Bandwidth_Control_1280", "Bandwidth_Control_1300",
                 "Bandwidth_Control_1870", "Bandwidth_Control_1880", "Bandwidth_Control_1900",
                 "wds_0020", "wds_0140", "wds_0160", "wds_0180", "wds_0200", "wds_0220", "wds_0240", "wds_0260", "wds_0280", "wds_0300",
                 "802.11a_b_g_n_0040", "802.11a_b_g_n_0050", "802.11a_b_g_n_0060", "802.11a_b_g_n_0120", "802.11a_b_g_n_0150", "802.11a_b_g_n_0200",
                 "802.11a_b_g_n_0210", "802.11a_b_g_n_0220", "802.11a_b_g_n_0230", "802.11a_b_g_n_0240", "802.11a_b_g_n_0270", "802.11a_b_g_n_0290",
                 "802.11a_b_g_n_0340", "802.11a_b_g_n_0360", "802.11a_b_g_n_0380",
                 "location_0110",
                 "定时关断射频_0110", "定时关断射频_0140", "定时关断射频_0160", "定时关断射频_0170", "定时删除SSID_0020", "定时删除SSID_0040", "定时删除SSID_0060",
                 "无线接口管理_0040",  "无线接口管理_0310", "无线接口管理_0380", "无线接口管理_0420",
                 "最大用户数限制_0040", "最大用户数限制_0050", "最大用户数限制_0060",
                 "频点设置0020", "频点设置0050",
                ], 
                #******************************************60A******************************************
                #******************************************80S******************************************
                [
                 #业务问题
                 "NAT-interface_0270", "Restore_Factory_Default_0030",
                 #命令行
                 "AC发现方式-0010", "断网保活_0010", 
                 "Station_Management_0010", "Station_Management_0020", "Station_Management_0030", "Station_Management_0040", "Station_Management_0050",
                 "Station_Management_0060","Station_Management_0070",
                 "AP_VLAN_0040",
                 "NAT-interface_0050", "NAT-interface_0060", "NAT-interface_0070",
                 "Bandwidth_Control_0010", "Bandwidth_Control_0020", "Bandwidth_Control_0030", "Bandwidth_Control_0040", "Bandwidth_Control_0050", 
                 "Bandwidth_Control_0060", "Bandwidth_Control_0070", "Bandwidth_Control_0080", "Bandwidth_Control_0090", "Bandwidth_Control_0100", 
                 "Bandwidth_Control_0110", "Bandwidth_Control_0120",
                 "802.11a_b_g_n_0080", "802.11a_b_g_n_0090", "802.11a_b_g_n_0100",
                 "802.11n_ac_0010", "802.11n_ac_0020", "802.11n_ac_0030", "802.11n_ac_0040", "802.11n_ac_0050",
                 "Hide_SSID_0030",
                 "中文SSID_0030", "中文SSID_0040",
                 #不支持
                 "wds*", "local_ip_acl*", "DTLS*", "自动频点和功率调整*", "Rogue*", "Wlan_dos*",
                 "AP_VLAN_0280", "AP_VLAN_0300", "AP_VLAN_0310", "AP_VLAN_0330", "AP_VLAN_0350", "AP_VLAN_0360",
                 "NAT-interface_0150", "断网保活_0640", "无线接口管理_0190",
                 #集中转发
                 "Webportal_in_8023tunel*",
                 "Forward_Mode_0030", "Forward_Mode_0050", "Forward_Mode_0270", "Forward_Mode_0280", "Forward_Mode_0290", "Forward_Mode_0300",
                 "Forward_Mode_0310", "Forward_Mode_0340", "Forward_Mode_0350", "Forward_Mode_0390",
                 "Station_Management_0110", "Station_Management_0120", "Station_Management_0130", "Station_Management_0140", "Station_Management_0150",
                 "Station_Management_0160", "Station_Management_0170", "Station_Management_0180", "Station_Management_0190", "Station_Management_0200",
                 "Station_Management_0210", "Station_Management_0220", "Station_Management_0230", "Station_Management_0250", "Station_Management_0260",
                 "Station_Management_0270", "Station_Management_0280", "Station_Management_0290", "Station_Management_0300", "Station_Management_0310",
                 "Station_Management_0320", "Station_Management_0330", "Station_Management_0340", "Station_Management_0350", "Station_Management_0360",
                 "Station_Management_0370", "Station_Management_0380", "Station_Management_0390", "Station_Management_0400", "Station_Management_0410",
                 "Station_Management_0430", "Station_Management_0440", "Station_Management_0450", "Station_Management_0460", "Station_Management_0470",
                 "Station_Management_0480", "Station_Management_0490", "Station_Management_0500", "Station_Management_0510", "Station_Management_0520", 
                 "Station_Management_0530", "Station_Management_0540", "Station_Management_0550", "Station_Management_0560", "Station_Management_0570",
                 "Station_Management_0580", "Station_Management_0590", "Station_Management_0600", "Station_Management_0610", "Station_Management_0690",
                 "Station_Management_0730", "Station_Management_0770", "Station_Management_0810", "Station_Management_0930", "Station_Management_1370",
                 "Station_Management_1380", "Station_Management_1390", "Station_Management_1400", "Station_Management_1450",
                 "AP_VLAN_0090", "AP_VLAN_0100", "AP_VLAN_0190", "AP_VLAN_0240", "AP_VLAN_0400", "AP_VLAN_0440", "AP_VLAN_0490", "AP_VLAN_0540",
                 "MTU_0100",
                 "Bandwidth_Control_0570", "Bandwidth_Control_0580", "Bandwidth_Control_0590", "Bandwidth_Control_0600", "Bandwidth_Control_0610", 
                 "Bandwidth_Control_0620", "Bandwidth_Control_0630", "Bandwidth_Control_0640", "Bandwidth_Control_0650", "Bandwidth_Control_0660", 
                 "Bandwidth_Control_0670", "Bandwidth_Control_0680", "Bandwidth_Control_0690", "Bandwidth_Control_0700", "Bandwidth_Control_0710", 
                 "Bandwidth_Control_0720", "Bandwidth_Control_0730", "Bandwidth_Control_0740", "Bandwidth_Control_0750", "Bandwidth_Control_0760", 
                 "Bandwidth_Control_0770", "Bandwidth_Control_0780", "Bandwidth_Control_0790", "Bandwidth_Control_0800", "Bandwidth_Control_0810", 
                 "Bandwidth_Control_0820", "Bandwidth_Control_0830", "Bandwidth_Control_0840", "Bandwidth_Control_0850", "Bandwidth_Control_0860", 
                 "Bandwidth_Control_0870", "Bandwidth_Control_0880", "Bandwidth_Control_1070", "Bandwidth_Control_1080", "Bandwidth_Control_1090", 
                 "Bandwidth_Control_1100", "Bandwidth_Control_1150", "Bandwidth_Control_1160", "Bandwidth_Control_1170", "Bandwidth_Control_1180", 
                 "Bandwidth_Control_1310", "Bandwidth_Control_1320", "Bandwidth_Control_1330", "Bandwidth_Control_1340", "Bandwidth_Control_1390", 
                 "Bandwidth_Control_1400", "Bandwidth_Control_1410", "Bandwidth_Control_1420",
                 "Local_DHCP_0150", "Local_DHCP_0160",
                 "二层隔离_0040", "二层隔离_0050", "二层隔离_0060", "二层隔离_0090",
                ],
                #******************************************80S******************************************
                #******************************************sonoma******************************************
                [
                 #业务问题
                 "NAT-interface_0270", "Restore_Factory_Default_0030",
                 #命令行
                 "AC发现方式-0010", "断网保活_0010", 
                 "Station_Management_0010", "Station_Management_0020", "Station_Management_0030", "Station_Management_0040", "Station_Management_0050",
                 "Station_Management_0060","Station_Management_0070",
                 "AP_VLAN_0040",
                 "NAT-interface_0050", "NAT-interface_0060", "NAT-interface_0070",
                 "Bandwidth_Control_0010", "Bandwidth_Control_0020", "Bandwidth_Control_0030", "Bandwidth_Control_0040", "Bandwidth_Control_0050", 
                 "Bandwidth_Control_0060", "Bandwidth_Control_0070", "Bandwidth_Control_0080", "Bandwidth_Control_0090", "Bandwidth_Control_0100", 
                 "Bandwidth_Control_0110", "Bandwidth_Control_0120",
                 "802.11a_b_g_n_0080", "802.11a_b_g_n_0090", "802.11a_b_g_n_0100",
                 "802.11n_ac_0010", "802.11n_ac_0020", "802.11n_ac_0030", "802.11n_ac_0040", "802.11n_ac_0050",
                 "Hide_SSID_0030",
                 "中文SSID_0030", "中文SSID_0040",
                 #不支持
                 "wds*", "local_ip_acl*", "DTLS*", "自动频点和功率调整*", "Rogue*", "Wlan_dos*",
                 "AP_VLAN_0280", "AP_VLAN_0300", "AP_VLAN_0310", "AP_VLAN_0330", "AP_VLAN_0350", "AP_VLAN_0360",
                 "NAT-interface_0150", "断网保活_0640", "无线接口管理_0190",
                 #集中转发
                 "Webportal_in_8023tunel*",
                 "Forward_Mode_0030", "Forward_Mode_0050", "Forward_Mode_0270", "Forward_Mode_0280", "Forward_Mode_0290", "Forward_Mode_0300",
                 "Forward_Mode_0310", "Forward_Mode_0340", "Forward_Mode_0350", "Forward_Mode_0390",
                 "Station_Management_0110", "Station_Management_0120", "Station_Management_0130", "Station_Management_0140", "Station_Management_0150",
                 "Station_Management_0160", "Station_Management_0170", "Station_Management_0180", "Station_Management_0190", "Station_Management_0200",
                 "Station_Management_0210", "Station_Management_0220", "Station_Management_0230", "Station_Management_0250", "Station_Management_0260",
                 "Station_Management_0270", "Station_Management_0280", "Station_Management_0290", "Station_Management_0300", "Station_Management_0310",
                 "Station_Management_0320", "Station_Management_0330", "Station_Management_0340", "Station_Management_0350", "Station_Management_0360",
                 "Station_Management_0370", "Station_Management_0380", "Station_Management_0390", "Station_Management_0400", "Station_Management_0410",
                 "Station_Management_0430", "Station_Management_0440", "Station_Management_0450", "Station_Management_0460", "Station_Management_0470",
                 "Station_Management_0480", "Station_Management_0490", "Station_Management_0500", "Station_Management_0510", "Station_Management_0520", 
                 "Station_Management_0530", "Station_Management_0540", "Station_Management_0550", "Station_Management_0560", "Station_Management_0570",
                 "Station_Management_0580", "Station_Management_0590", "Station_Management_0600", "Station_Management_0610", "Station_Management_0690",
                 "Station_Management_0730", "Station_Management_0770", "Station_Management_0810", "Station_Management_0930", "Station_Management_1370",
                 "Station_Management_1380", "Station_Management_1390", "Station_Management_1400", "Station_Management_1450",
                 "AP_VLAN_0090", "AP_VLAN_0100", "AP_VLAN_0190", "AP_VLAN_0240", "AP_VLAN_0400", "AP_VLAN_0440", "AP_VLAN_0490", "AP_VLAN_0540",
                 "MTU_0100",
                 "Bandwidth_Control_0570", "Bandwidth_Control_0580", "Bandwidth_Control_0590", "Bandwidth_Control_0600", "Bandwidth_Control_0610", 
                 "Bandwidth_Control_0620", "Bandwidth_Control_0630", "Bandwidth_Control_0640", "Bandwidth_Control_0650", "Bandwidth_Control_0660", 
                 "Bandwidth_Control_0670", "Bandwidth_Control_0680", "Bandwidth_Control_0690", "Bandwidth_Control_0700", "Bandwidth_Control_0710", 
                 "Bandwidth_Control_0720", "Bandwidth_Control_0730", "Bandwidth_Control_0740", "Bandwidth_Control_0750", "Bandwidth_Control_0760", 
                 "Bandwidth_Control_0770", "Bandwidth_Control_0780", "Bandwidth_Control_0790", "Bandwidth_Control_0800", "Bandwidth_Control_0810", 
                 "Bandwidth_Control_0820", "Bandwidth_Control_0830", "Bandwidth_Control_0840", "Bandwidth_Control_0850", "Bandwidth_Control_0860", 
                 "Bandwidth_Control_0870", "Bandwidth_Control_0880", "Bandwidth_Control_1070", "Bandwidth_Control_1080", "Bandwidth_Control_1090", 
                 "Bandwidth_Control_1100", "Bandwidth_Control_1150", "Bandwidth_Control_1160", "Bandwidth_Control_1170", "Bandwidth_Control_1180", 
                 "Bandwidth_Control_1310", "Bandwidth_Control_1320", "Bandwidth_Control_1330", "Bandwidth_Control_1340", "Bandwidth_Control_1390", 
                 "Bandwidth_Control_1400", "Bandwidth_Control_1410", "Bandwidth_Control_1420",
                 "Local_DHCP_0150", "Local_DHCP_0160",
                 "二层隔离_0040", "二层隔离_0050", "二层隔离_0060", "二层隔离_0090",
                ]
                #******************************************sonoma******************************************
               ]

import os
import time
import re

def get_exclude_file_use_list(listvar):
    re_var = []
    non_var = []
    for i in listvar:
        if "*" in i:
            re_var.append(i)
        else:
            non_var.append(i + ".txt")
    return re_var, non_var
    
#@deprecated
def get_exlude_file(path):
    re_exclude_list = []
    exclude_list_file = []
    fp = open(path, "r")
    for i in fp:
        if "*" in i:
            re_exclude_list.append(i.split("\n")[0])
            continue
        exclude_list_file.append(i.split("\n")[0] + ".txt")
    fp.close()
    return re_exclude_list, exclude_list_file

def get_file_list(path):
    xl = []
    re_st = os.listdir(path)
    for i in re_st:
        j = i
        i = os.path.join(path, i)
        if os.path.isdir(i):
            xl += get_file_list(i)
        else:
            if (j not in exclude_spc_file) and (os.path.splitext(j)[1] not in exclude_suffix):
                xl.append(j)
    return xl

def main(basefile, cmpfilelist, excfilelist, resultlist):
    base_list_file = get_file_list(basefile)
    print  "+" * 30 + "base_file total: %d" % len(base_list_file)
    time.sleep(1)
    for k in range(len(cmpfilelist)):
        need_sync = []
        no_sync = []
        cmp_list_file = get_file_list(cmpfilelist[k])
        print  "+" * 30 + "%s total: %d  %d-%d=%d" % (os.path.split(cmpfilelist[k])[-1] ,len(cmp_list_file), len(base_list_file), 
            len(cmp_list_file), len(base_list_file) - len(cmp_list_file)),
        time.sleep(1)
        (re_exclude_list, exclude_list_file) = get_exclude_file_use_list(excfilelist[k])
        time.sleep(1)
        if os.path.exists(resultlist[k]):
            os.remove(resultlist[k])
        
        for i in base_list_file:
            reflag = False
            if (i not in cmp_list_file) and (i not in exclude_list_file):
                if len(re_exclude_list):
                    for j in re_exclude_list:
                        if re.search(j, i, re.I):
                            reflag = True
                            break
                if not reflag:
                    need_sync.append(i)
        
        for m in base_list_file:
            if (m not in need_sync) and (m not in cmp_list_file):
                no_sync.append(m)
        
        print "  non support: %d" % len(no_sync),
        print "  need sync: %d" % len(need_sync)
        
        fp = open(resultlist[k], "a")
        fp.write(str(len(need_sync)))
        fp.write("\n")
        for i in need_sync:
            fp.write(i + "\n")
        fp.write("*"*60 + "no support" + "*"*60 + "\n")
        fp.write(str(len(no_sync)))
        fp.write("\n")
        for i in no_sync:
            fp.write(i + "\n")
        fp.close()

if __name__ == "__main__":
    main(base_file, cmp_file, exclude_file, result_file)
