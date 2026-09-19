#!/usr/bin/env python3


class MinimalTheme:
    # ----------------------
    ST_BN1_NAME = 'Repo'
    ST_BN1_URL = 'https://github.com/obscure-n8'
    ST_BN2_NAME = 'Owner'
    ST_BN2_URL = 'https://github.com/obscure-n8'
    ST_MSG = (
        '<b><i>This bot can mirror all your links | files | torrents '
        'to Telegram with Leech | Mirror | VT Convert | Archive support.</i>\n\n'
        'Type {help_command} to get a list of available commands</b>'
    )
    ST_BOTPM = '<i>Now, This bot will send all your files and links here. Start Using ...</i>'
    ST_UNAUTH = '<i>You Are not authorized user! Deploy your own ZxZone Mirror-Leech bot</i>'
    OWN_TOKEN_GENERATE = '<b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i>'
    USED_TOKEN = '<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'
    LOGGED_PASSWORD = '<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>'
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = (
        '<b><u>Generated Temporary Login Token!</u></b>\n'
        '<b>Temp Token:</b> <code>{token}</code>\n'
        '<b>Validity:</b> {validity}'
    )
    # ----------------------
    ACTIVATED = 'Activated'
    # ----------------------
    LOGGED_IN = '<b>Already Bot Login In!</b>'
    INVALID_PASS = '<b>Invalid Password!</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully!</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ----------------------
    LOG_DISPLAY_BT = 'Log Display'
    WEB_PASTE_BT = 'Web Paste (SB)'
    # ----------------------
    BASIC_BT = 'Basic'
    USER_BT = 'Users'
    MICS_BT = 'Mics'
    O_S_BT = 'Owner & Sudos'
    CLOSE_BT = 'Close'
    HELP_HEADER = (
        'Help Guide Menu!\n\n'
        '<b>NOTE: <i>Click on any CMD to see more minor details.</i></b>'
    )

    
⌬ 𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗦 = '''BOT STATISTICS :
Bot Uptime : {bot_uptime}

RAM ( MEMORY ) :
{ram_bar} {ram}%
U : {ram_u} | F : {ram_f} | T : {ram_t}

SWAP MEMORY :
{swap_bar} {swap}%
U : {swap_u} | F : {swap_f} | T : {swap_t}

DISK :
{disk_bar} {disk}%
Total Disk Read : {disk_read}
Total Disk Write : {disk_write}
U : {disk_u} | F : {disk_f} | T : {disk_t}
'''
    SYS_STATS = '''OS SYSTEM :
OS Uptime : {os_uptime}
OS Version : {os_version}
OS Arch : {os_arch}

NETWORK STATS :
Upload Data: {up_data}
Download Data: {dl_data}
Pkts Sent: {pkt_sent}k
Pkts Received: {pkt_recv}k
Total I/O Data: {tl_data}

CPU :
{cpu_bar} {cpu}%
CPU Frequency : {cpu_freq}
System Avg Load : {sys_load}
P-Core(s) : {p_core} | V-Core(s) : {v_core}
Total Core(s) : {total_core}
Usable CPU(s) : {cpu_use}
'''
    REPO_STATS = '''REPO STATISTICS :
Bot Updated : {last_commit}
Current Version : {bot_version}
Latest Version : {lat_version}
Last ChangeLog : {commit_details}

REMARKS : <code>{remarks}</code>
'''
    BOT_LIMITS = '''BOT LIMITATIONS :
Direct Limit : {DL} GB
Torrent Limit : {TL} GB
GDrive Limit : {GL} GB
YT-DLP Limit : {YL} GB
Playlist Limit : {PL}
Mega Limit : {ML} GB
Clone Limit : {CL} GB
Leech Limit : {LL} GB

Token Validity : {TV}
User Time Limit : {UTI} / task
User Parallel Tasks : {UT}
Bot Parallel Tasks : {BT}
'''
    # ----------------------

    RESTARTING = '<i>Restarting...</i>'
    # ----------------------

    RESTART_SUCCESS = '''Restarted Successfully!
Date: {date}
Time: {time}
TimeZone: {timz}
Version: {version}'''
    RESTARTED = 'Bot Restarted!'
    # ----------------------

    PING = '<i>Starting Ping..</i>'
    PING_VALUE = '<b>Pong</b>\n<code>{value} ms..</code>'
    # ----------------------

    LINKS_START = '''<b><i>Task Started</i></b>
Mode: {Mode}
By: {Tag}

'''
    LINKS_SOURCE = '''Source:
Added On: {On}
------------------------------------------
{Source}
------------------------------------------

'''

    # ----------------------
    PM_START = "Task Started :\nLink: <a href='{msg_link}'>Click Here</a>"
    L_LOG_START = (
        "Leech Started :\n"
        "User : {mention} ( #ID{uid} )\n"
        "Source : <a href='{msg_link}'>Click Here</a>"
    )

    NAME = '{Name}\n'
    SIZE = 'Size: {Size}\n'
    ELAPSE = 'Elapsed: {Time}\n'
    MODE = 'Mode: {Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES = 'Total Files: {Files}\n'
    L_CORRUPTED_FILES = 'Corrupted Files: {Corrupt}\n'
    L_CC = 'By: {Tag}\n\n'
    PM_BOT_MSG = 'File(s) have been Sent above'
    L_BOT_MSG = 'File(s) have been Sent to Bot PM (Private)'
    L_LL_MSG = 'File(s) have been Sent. Access via Links...\n'

    # ----- MIRROR -------
    M_TYPE = 'Type: {Mimetype}\n'
    M_SUBFOLD = 'SubFolders: {Folder}\n'
    TOTAL_FILES = 'Files: {Files}\n'
    RCPATH = 'Path: <code>{RCpath}</code>\n'
    M_CC = 'By: {Tag}\n\n'
    M_BOT_MSG = 'Link(s) have been Sent to Bot PM (Private)'

    # ----- BUTTONS -------
    CLOUD_LINK = 'Cloud Link'
    SAVE_MSG = 'Save Message'
    RCLONE_LINK = 'RClone Link'
    DDL_LINK = '{Serv} Link'
    SOURCE_URL = 'Source Link'
    INDEX_LINK_F = 'Index Link'
    INDEX_LINK_D = 'Index Link'
    VIEW_LINK = 'View Link'
    CHECK_PM = 'View in Bot PM'
    CHECK_LL = 'View in Links Log'
    MEDIAINFO_LINK = 'MediaInfo'
    SCREENSHOTS = 'ScreenShots'
    # ----------------------

    # ----------------------
    STATUS_NAME = '{Name}'

    BAR = '\n{Bar}'
    PROCESSED = '\nProcessed: {Processed}'
    STATUS = '\nStatus: <a href="{Url}">{Status}</a>'
    ETA = ' | ETA: {Eta}'
    SPEED = '\nSpeed: {Speed}'
    ELAPSED = ' | Elapsed: {Elapsed}'
    ENGINE = '\nEngine: {Engine}'
    STA_MODE = '\nMode: {Mode}'
    SEEDERS = '\nSeeders: {Seeders} | '
    LEECHERS = 'Leechers: {Leechers}'

    SEED_SIZE = '\nSize: {Size}'
    SEED_SPEED = '\nSpeed: {Speed} | '
    UPLOADED = 'Uploaded: {Upload}'
    RATIO = '\nRatio: {Ratio} | '
    TIME = 'Time: {Time}'
    SEED_ENGINE = '\nEngine: {Engine}'

    STATUS_SIZE = '\nSize: {Size}'
    NON_ENGINE = '\nEngine: {Engine}'

    USER = '\nUser: <code>{User}</code> | '
    ID = 'ID: <code>{Id}</code>'
    BTSEL = '\nSelect: {Btsel}'
    CANCEL = '\n{Cancel}\n\n'

    FOOTER = 'Bot Stats\n'
    TASKS = 'Tasks: {Tasks}\n'
    BOT_TASKS = 'Tasks: {Tasks}/{Ttask} | AVL: {Free}\n'
    Cpu = 'CPU: {cpu}% | '
    FREE = 'F: {free} [{free_p}%]'
    Ram = '\nRAM: {ram}% | '
    uptime = 'UPTIME: {uptime}'
    DL = '\nDL: {DL}/s | '
    UL = 'UL: {UL}/s'

    PREVIOUS = '<<'
    REFRESH = 'PAGES {Page}'
    NEXT = '>>'
    # ----------------------

    STOP_DUPLICATE = (
        'File/Folder is already available in Drive.\n'
        'Here are {content} list results:'
    )
    # ----------------------

    COUNT_MSG = 'Counting: <code>{LINK}</code>'
    COUNT_NAME = '{COUNT_NAME}\n'
    COUNT_SIZE = 'Size: {COUNT_SIZE}\n'
    COUNT_TYPE = 'Type: {COUNT_TYPE}\n'
    COUNT_SUB = 'SubFolders: {COUNT_SUB}\n'
    COUNT_FILE = 'Files: {COUNT_FILE}\n'
    COUNT_CC = 'By: {COUNT_CC}\n'
    # ----------------------

    LIST_SEARCHING = 'Searching for {NAME}'
    LIST_FOUND = 'Found {NO} result for {NAME}'
    LIST_NOT_FOUND = 'No result found for {NAME}'
    # ----------------------

    NO_ACTIVE_DL = '''<i>No Active Downloads!</i>

BOT STATS
CPU: {cpu}% | F: {free} [{free_p}%]
RAM: {ram} | UPTIME: {uptime}
'''
    # ----------------------

    USER_SETTING = '''User Settings :

Name : {NAME} ( <code>{ID}</code> )
Username : {USERNAME}
Telegram DC : {DC}
Language : {LANG}

Available Args:
- -s or -set : Set Directly via Arg'''

    UNIVERSAL = '''Universal Settings : {NAME}

YT-DLP Options : <code>{YT}</code>
Daily Tasks : <code>{DT}</code> per day
Last Bot Used : <code>{LAST_USED}</code>
User Session : <code>{USESS}</code>
MediaInfo Mode : <code>{MEDIAINFO}</code>
Save Mode : <code>{SAVE_MODE}</code>
User Bot PM : <code>{BOT_PM}</code>'''

    MIRROR = '''Mirror/Clone Settings : {NAME}

RClone Config : <i>{RCLONE}</i>
Mirror Prefix : <code>{MPREFIX}</code>
Mirror Suffix : <code>{MSUFFIX}</code>
Mirror Remname : <code>{MREMNAME}</code>
DDL Server(s) : <i>{DDL_SERVER}</i>
User TD Mode : <i>{TMODE}</i>
Total User TD(s) : <i>{USERTD}</i>
Daily Mirror : <code>{DM}</code> per day'''

    LEECH = '''Leech Settings for {NAME}

Daily Leech : <code>{DL}</code> per day
Leech Type : <i>{LTYPE}</i>
Custom Thumbnail : <i>{THUMB}</i>
Leech Split Size : <code>{SPLIT_SIZE}</code>
Equal Splits : <i>{EQUAL_SPLIT}</i>
Media Group : <i>{MEDIA_GROUP}</i>
Leech Caption : <code>{LCAPTION}</code>
Leech Prefix : <code>{LPREFIX}</code>
Leech Suffix : <code>{LSUFFIX}</code>
Leech Remname : <code>{LREMNAME}</code>
Leech Dumps : <code>{LDUMP}</code>
Leech Attachment : <code>{ATTACHMENT}</code>
Leech Metadata : <code>{METADATA}</code>'''
