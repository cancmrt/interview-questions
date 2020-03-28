from bs4 import BeautifulSoup
class Table:
    def __init__(self):
        self.Page = None
        self.Columns = None
        self.Rows = None
        self.RemovedLeft = []
        self.SoapTable = None

class TableEngine:
    def __init__(self,Page):
        self.Page = Page
        self.THeadExist = False
        self.RemoveFromLeft = False
        self.Tables = []
        self.RowSpan = []
        self.RemovedLeft = []
        PureTables = self.Page.Content.findAll("table")
        self.__TableMergeMe(PureTables)
    def __TableMergeMe(self,PureTables):
        if len(PureTables) > 1:
            mid = int(len(PureTables) / 2)

            leftTables = PureTables[:mid]
            rightTables = PureTables[mid:]

            self.__TableMergeMe(leftTables)
            self.__TableMergeMe(rightTables)
        pTable = PureTables[0]
        NewTable = Table()
        NewTable.Page = self.Page
        NewTable.Columns = self.__GetColumns(pTable)
        NewTable.Rows = self.__GetRows(pTable,NewTable.Columns)
        NewTable.RemovedLeft = self.RemovedLeft
        NewTable.SoapTable = pTable
        self.Tables.append(NewTable)
        self.RemovedLeft = []
    def __GetColumns(self, Soap):
        THead = Soap.find("thead")
        TBody = Soap.find("tbody")
        Body = None
        Columns = []
        if THead != None:
            Body = THead.find("tr").findAll("td")
            self.THeadExist = True
        elif TBody != None:
            Body = TBody.find("tr").findAll("td")
            self.THeadExist = False
        else:
            Body = Soap.find("tr").findAll("td")
            self.THeadExist = False

        for td in Body:
            if td.text:
                Columns.append(td.text)
        if len(Columns) != len(Body):
            self.RemoveFromLeft = True
        return Columns
    def __GetRows(self,Soap,Columns):
        Body = Soap.find("tbody")
        if Body == None:
            Body = Soap

        TableColumnCount = len(Columns)
        TableRowCount =  len(Body.findAll("tr"))
        if self.THeadExist != True:
            TableRowCount = TableRowCount - 1
        
        Matrix = [[None for x in range(TableColumnCount)] for y in range(TableRowCount)]
        MatrixIndexer = [y for y in range(TableRowCount)]
        
        BodyTr = Body.findAll("tr")
        BodyTr.pop(0)

        self.__RowMergeMe(BodyTr,Matrix,MatrixIndexer)

        for span in self.RowSpan:
            TakenData = Matrix[span.RowIndex-1][span.ElementIndex]
            Matrix[span.RowIndex][span.ElementIndex] = TakenData
        return Matrix

    
    def __RowMergeMe(self,Array,Matrix,MatrixIndexer):
        if len(Array) > 1:
            mid = int(len(Array) / 2)

            leftArray = Array[:mid]
            leftMatrix = Matrix[:mid]
            rightArray = Array[mid:]
            rightMatrix = Matrix[mid:]
            leftMatrixIndexer = MatrixIndexer[:mid]
            rightMatrixIndexer = MatrixIndexer[mid:]

            self.__RowMergeMe(leftArray,leftMatrix,leftMatrixIndexer)
            self.__RowMergeMe(rightArray,rightMatrix,rightMatrixIndexer)
        TrTd = Array[0].findAll("td")
        if self.RemoveFromLeft:
            self.RemovedLeft.append(TrTd.pop(0).text)
        ColSpanValue = 0
        ColSpanIndex = 0
        RowSpanValue = 0
        RowSpanIndex = 0
        for i in range(0,len(Matrix[0])):
            if i < len(TrTd):
                GetColSpan = TrTd[i].get("colspan")
                GetRowSpan = TrTd[i].get("rowspan")
                NormalTd = True
                if GetRowSpan != None:
                    RowSpanValue = int(GetRowSpan) - 1
                    RowSpanIndex = i
                if RowSpanValue != 0 and RowSpanIndex >= i:
                    if len(Matrix[0]) > i+1:
                        Matrix[0][i+1] =TrTd[i].text
                        RowSpanIndex = RowSpanIndex - 1
                        NormalTd = False
                if GetColSpan != None:
                    ColSpanValue = int(GetColSpan) - 1
                    ColSpanIndex = i
                elif ColSpanValue != 0 and ColSpanIndex != i:
                    Matrix[0][i] = Matrix[0][i-1]
                    ColSpanValue = ColSpanValue - 1
                    NormalTd = False
                
                if NormalTd:
                    Matrix[0][i] = TrTd[i].text
            elif Matrix[0][i] == None:
                rowspan = RowSpanElement(MatrixIndexer[0],i)
                self.RowSpan.append(rowspan)
class RowSpanElement:
    def __init__(self,RowIndex,ElementIndex):
        self.RowIndex = RowIndex
        self.ElementIndex = ElementIndex