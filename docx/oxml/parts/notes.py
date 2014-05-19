from docx.oxml.shared import OxmlBaseElement, qn
#from docx.oxml.text import CT_P


class CT_Notes(OxmlBaseElement):
    
    _notes_tag = None
    
    @property
    def notes_lst(self):
        return self.findall(self._notes_tag)
    

class CT_Endnotes(CT_Notes):
    _notes_tag = qn('w:endnote')


class CT_Footnotes(CT_Notes):
    _notes_tag = qn('w:footnote')
    

class CT_Note(OxmlBaseElement):
    
    @property
    def type(self):
        return self.attrib.get(qn('w:type'))
    
    @property
    def id(self):
        return int(self.attrib.get(qn('w:id')))
    
    @property
    def p_lst(self):
         return self.findall(qn('w:p'))
     
