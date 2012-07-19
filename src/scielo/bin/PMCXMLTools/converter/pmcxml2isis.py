import os
import sys

from xml2json_converter import XML2JSONConverter
from json2id import JSON2IDFile
from id2isis import IDFile2ISIS


from report import Report
from parameters import Parameters
from my_files import MyFiles

my_files = MyFiles()


class PMCXML2ISIS:

    def __init__(self, records_order, id2isis, xml2json_table_filename = '_pmcxml2isis.txt'):
       self.xml2json_table_filename = xml2json_table_filename
       self.records_order = records_order
       self.tables = {}
       self.id2isis = id2isis
       
       
    def generate_json(self, xml_filename, supplementary_xml_filename, report):
        xml2json_converter = XML2JSONConverter(self.xml2json_table_filename, report)
        json_data = xml2json_converter.convert(xml_filename)
        return json_data
            
    def generate_id_file(self, json_data, id_filename, report):
        id_file = JSON2IDFile(id_filename, report)
        id_file.format_records_and_save(self.records_order, json_data)
        
    def generate_id_file_list(self, files_set, report):
        
        cmd = ''
        files_set.prepare()
        id_filename_list = []
        list = os.listdir(files_set.xml_path)
        for f in list:
            if '.xml' in f:
                xml_filename = files_set.xml_path + '/' + f
                id_filename = f.replace('.xml', '.id')
                
                json_data = self.generate_json(xml_filename, files_set.suppl_filename, report)
                #self.generate_id_file(json_data, files_set.output_path + '/' + id_filename, report)
                
    def convert_id_files_to_mst(self, db_path, db_name, script_filename, report):
        cmds = self.id2isis.create_script_content(db_path, db_name, report)
        self.id2isis.run_commands(cmds)
        if not os.path.exists(db_path + '/' + db_name + '.mst'):
            self.id2isis.run_commands(cmds, True)
        if not os.path.exists(db_path + '/' + db_name + '.mst'):
            self.id2isis.write_script(script_filename + '.bat', cmds)
            self.id2isis.write_script(script_filename + '.sh', cmds)
            
    def execute(self, xml_path, suppl_filename, output_path, db_name, script_filename, debug_depth, display_on_screen):
        files_set = PMCXML_FilesSet(xml_path, suppl_filename, output_path, db_name)
        report = Report(files_set.log_filename, files_set.err_filename, debug_depth, display_on_screen) 
        self.generate_id_file_list(files_set, report)
        self.convert_id_files_to_mst(output_path, db_name, output_path + '/'+ script_filename, report)
        
class PMCXML_FilesSet:

    def __init__(self, xml_path, suppl_filename, output_path, db_name):
        self.xml_path = xml_path
        self.output_path = output_path
        self.db_name = db_name
        self.db_filename = output_path + '/' + db_name
        self.suppl_filename = suppl_filename
        self.log_filename = output_path + '/' + db_name + '.log'
        self.err_filename = output_path + '/' + db_name + '.err.log'
        
    
    def prepare(self):
        if os.path.exists(self.output_path):
            files = os.listdir(self.output_path)
            for f in files:
                print('deleting ' + self.output_path + '/' + f + '?')
                ext = f[f.rfind('.'):]
                if ext in ['.id', '.mst', '.xrf', '.log', ]:
                    print('deleting ' + self.output_path + '/' + f)
                    #os.remove(self.output_path + '/' + f)
        else:
            os.makedirs(self.output_path)
    
                
if __name__ == '__main__':
    parameter_list = ['', 'path of XML files', 'supplementary XML', 'output path', 'database name (no extension)', 'batch and shell script filename to generate .mst database name (no extension)', 'cisis path', 'debug_depth', 'display messages on screen? yes|no']
    parameters = Parameters(parameter_list)
    if parameters.check_parameters(sys.argv):
    	this_script_name, xml_path, suppl_xml, output_path, db_name, script_filename, cisis_path, debug_depth, display_on_screen = sys.argv
        
        output_path = output_path.replace('\\', '/')
        xml_path = xml_path.replace('\\', '/')
        
        pmcxml2isis = PMCXML2ISIS('hr', IDFile2ISIS(cisis_path), '_pmcxml2isis.txt')
        pmcxml2isis.execute(xml_path, suppl_xml, output_path, db_name, script_filename, int(debug_depth), (display_on_screen == 'yes'))
        
        
    
    