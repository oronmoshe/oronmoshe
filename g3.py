""""""
"load exel file csv format , and jinja2 to python "
""""""
import csv
from jinja2 import Template

""""""
"name of csv and jinja file ,should be in the pycharm directory "
""""""
source_file = "srx11.csv"
srx_template_file = "srx1.j2"

""""""
" 'with open' to read the cfg j2 file"
""""""
with open(srx_template_file) as f:
    cfg_srx_template = Template(f.read(), #keep_trailing_newline=True)

""""""
" 'with open' to read the csv file and make the dict to exel "
""""""

srx_configs = ""
with open(source_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        interface_config = cfg_srx_template.render(
            hostname=row["Koko"],
            interface=row["Interface"],
            vlan=row["Vlan"],
            server=row["Server"],
            link=row["Link"],
            purpose=row["Purpose"],
            ddd=row["Ddd"],
         )
        srx_configs += interface_config
""""""
"print to console"
""""""
print(srx_configs)
""""""
"make a source_file"
""""""
with open("srx_configs.txt", "w") as f:
    f.write(srx_configs)
