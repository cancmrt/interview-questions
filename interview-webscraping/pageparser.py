import requests
from bs4 import BeautifulSoup

class Page:
    def __init__(self,PageAddress):
        self.PageAddress = PageAddress
        self.Content = None
        self.PageName = None
        self.DownloadContent()
    def DownloadContent(self):
        response = requests.get(self.PageAddress)
        self.Content = BeautifulSoup(response.text, "html.parser")
        self.GetPageName()
    def GetPageName(self):
        self.PageName = self.Content.find("title").text
    def GetDefinitions(self,Selector):
        Info = []
        for item in Selector:
            if item.Rule != "" and item.Rule != None:
                selected = self.Content.find(item.Tag, item.Rule).text
                Info.append(selected)
            else:
                selected = self.Content.find(item.Tag).text
                Info.append(selected)
        return Info
class DefinitionSelector:
    def __init__(self,Tag,Rule):
        self.Tag = Tag
        self.Rule = Rule
