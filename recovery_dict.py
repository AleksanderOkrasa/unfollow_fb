
class RecoveryDict():
    def __init__(self):
        self.lines_list = []  #lista która będzie przechowywała linie
        self.one_line_with_all = ''  #wartość złączająca wszystkie elementy listy
        self.dict_elements_list = [] #lista zawierajaca elementy slownika
        self.dict = {}   #docelowa zmienna zawierająca poprzedni słownik przekazywany w inpucie

    def read_input_and_create_list(self, sign_of_end_last_line):
    #czytanie inputu, przekazywanie każdej linijki do listy
        while True:
            line = input()
            if line.endswith(sign_of_end_last_line):
                line = line.rstrip(sign_of_end_last_line)
                self.lines_list.append(line)
                break
            self.lines_list.append(line)

        return self.lines_list

    def join_elements_list(self):
    #złączenie wszystkich elementów listy w jeden ciąg (połączenie linków)
        for line in self.lines_list:
            self.one_line_with_all += line
        return self.one_line_with_all

    def split_one_line_to_dict_elements_list(self, sign_of_dividing_the_dictionary_into_elements):
    #podział długiego stringa na listę, gdzie każdy element to jeden klucz i wartość starego słownika
        self.dict_elements_list = self.one_line_with_all.split(sign_of_dividing_the_dictionary_into_elements)
        return self.dict_elements_list

    def extracting_the_key_and_value_from_the_list_of_dictionary_elements(self, sign_to_dive_dictionary_elements_into_key_and_value):
        for line in self.dict_elements_list:
            key_and_value = line.split(sign_to_dive_dictionary_elements_into_key_and_value)
            key = key_and_value[0]
            elements_of_value = key_and_value[1:]
            value = ''
            for element in elements_of_value:
                value += element + sign_to_dive_dictionary_elements_into_key_and_value
            key = key[2:-1]         #usunięcie " '" i "'"it
            value = value[2:-2]     #usunięcie " '" i " '"
            #print(f'klucz: {key}, wartość: {value}')
            self.dict[key] = value
        return self.dict


if __name__ == '__main__':

        recovery = RecoveryDict()
        recovery.read_input_and_create_list('}')
        recovery.join_elements_list()
        recovery.split_one_line_to_dict_elements_list(',')
        print(recovery.extracting_the_key_and_value_from_the_list_of_dictionary_elements(':'))


        # sign_of_end_last_line = '}'
        # sign_of_dividing_the_dictionary_into_elements = ','
        # sign_to_dive_dictionary_elements_into_key_and_value = ':'
