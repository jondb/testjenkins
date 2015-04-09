

#aa7de1c0e8e4a93fb86bbfd2f9559e04

import os

cmd = 'curl -XPOST http://pastebin.com/api/api_post.php -F"api_dev_key=aa7de1c0e8e4a93fb86bbfd2f9559e04" -F"api_option=paste" -F"api_paste_code=$(date)"'
print os.system(cmd)