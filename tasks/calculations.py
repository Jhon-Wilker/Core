

class Calculations():
    def quantidade(self,mylist_items):
        count = len(mylist_items)
        return count
    
    def total_pacotes(self, mylist_items):
        count = 0
        for itens in mylist_items:
            count += itens.contract_pack
        return count
    
    def total_chamadas(self, mylist_items):
        return sum(mylist_items.values())

    def total_valor(self,mylist_items):
        count = 0
        for itens in mylist_items:
            count += itens.contract_value
        return count
    
    def calc_unit(self,mylist_value,mylist_pack):
        unit = mylist_value / mylist_pack
        return unit
    
    def call_calc_unit(self,mylist_items):
        unit_dict={}
        for itens in mylist_items:
            unit_dict[itens.name] = self.calc_unit(itens.contract_value,itens.contract_pack)
        
        return unit_dict

    def convert_money(self,string):
        string = 'R$ {:,.2f}'.format(string)
        return string

    def convert_to_list(self, my_list):
        list_values= {}
        for i in my_list:
            list_values[i.name] = self.convert_money(i.contract_value)
        print(list_values)
        return list_values
