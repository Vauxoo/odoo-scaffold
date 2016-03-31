from openerp.tests.common import TransactionCase
import csv
import os


class TestInitData(TransactionCase):
    """
    Tests the init data of the module.
    """

    def setUp(self):
        super(TestInitData, self).setUp()
        self.imd_obj = self.registry('ir.model.data')
        # 'ir.model.data' model: (id, name, module, model, res_id)

    def test_init_data(self):
        """
        This method check in all the xml ids in the cvs files are loaded into
        the xml id in the openerp data base in table ir.model.data
        """
        cr, uid = self.cr, self.uid
        data_obj = data_integrity()
        load_err_msg = ('The record {xml_id} ({model}) was not loaded.')

        # get a list of the record data
        record_data = dict()
        for csv_file in data_obj.csv_list:
            csv_lines = data_obj.read_csv_file(csv_file)

            for line in csv_lines:
                record_xml_id = line[0].split('.')[-1]
                imd_id = self.imd_obj.search(
                    cr, uid,
                    [('model', '=', line[1]), ('name', '=', record_xml_id)])

                record_data.update(
                    model=line[1], xml_id=line[0], name=record_xml_id,
                    imd_id=imd_id)

                # check is the data in the csv files were loaded in the
                # openerp current instance

                self.assertEquals(
                    bool(record_data['imd_id']), True,
                    load_err_msg.format(**record_data))


class data_integrity(object):

    """
    Data Integrity methods.
    """

    def __init__(self):
        """
        Initializate the data integrity object This method read the config
        file and save the csv file names list to check.
        @return None
        """
        module_path = os.path.split(os.path.split(__file__)[0])[0]
        csv_path = os.path.join(module_path, 'data/csv_data')
        csv_files = list()
        for root, dirs, files in os.walk(csv_path):
            for f in files:
                if f.endswith(".csv"):
                    csv_files.append(os.path.join(root, f))
        self.csv_list = csv_files
        return None

    def read_csv_file(self, cvs_name):
        """
        This method read the data of a csv file.
        @retrun [(xml_id, model)]
        """
        lines = list()
        csv_lines = csv.DictReader(open(cvs_name))
        for line in csv_lines:
            # ditionary with the {field name: field value,}
            lines += [(line.pop('id'), line.pop('model'))]
        return lines[1:]
