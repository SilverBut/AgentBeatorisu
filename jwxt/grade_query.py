# -*- coding:utf-8 -*-
import bs4
import requests

class JwxtAction():
    def __init__(self, username, password):
        self.jwxt_url = 'http://jwxt.xidian.edu.cn'
        self.ids_url = 'http://ids.xidian.edu.cn'
        self.jwxt_grade_all = 'http://jwxt.xidian.edu.cn/bxqcjcxAction.do'
        self.jwxt_grade_failed = 'http://jwxt.xidian.edu.cn/gradeLnAllAction.do?type=ln&oper=bjg'
        self.jwxt_grade_passed = 'http://jwxt.xidian.edu.cn/gradeLnAllAction.do?type=ln&oper=qbinfo'
        self.login_info = {"username":username, "password":password}
        self.session = requests.Session()

    def login(self):
        if self.isLogined():
            return True
        jwxt_response = self.session.get( self.jwxt_url, allow_redirects = False )
        if not jwxt_response.is_redirect:
            raise Exception('Unknown response %s'%(jwxt_response.content.decode('gbk')))
        ids_response = self.session.send( jwxt_response.request )
        assert( ids_response.status_code == 200 )
        browser_parser = bs4.BeautifulSoup( ids_response.content.decode('utf-8-sig'), "html.parser" )
        login_form = browser_parser.find('form')
        login_info = self.login_info.copy()
        for input in login_form.findChildren('input'):
            if not login_info.get( input['name'] ):
                login_info[input['name']] = input['value']
        ids_loginurl = self.ids_url + login_form['action']
        ids_response = self.session.post( ids_loginurl, data=login_info , allow_redirects = True )
        return self.isLogined()

    def isLogined(self):
        jwxt_response = self.session.get( self.jwxt_url, allow_redirects = False )
        if jwxt_response.is_redirect:
            return False
        else:
            browser_parser = bs4.BeautifulSoup( jwxt_response.content.decode('gbk'), "html.parser" )
            if browser_parser.findChild('title').text == '学分制综合教务':
                return True
            else:
                raise Exception('Unknown response %s'%(jwxt_response.content.decode('gbk')))

    def checkIsLogined(func):
        def _checkIsLogined(self):
            if not self.isLogined():
                self.login()
            return func(self)
        return _checkIsLogined

    @checkIsLogined
    def get_grade_all(self):
        grade_info = []
        grade_head = []
        jwxt_response = self.session.get( self.jwxt_grade_all )
        browser_parser = bs4.BeautifulSoup( jwxt_response.content.decode('gbk'), "html.parser" )
        grade_parser = browser_parser.findChild(name='table' , attrs = {'id':'user'})
        assert(grade_parser != None)
        for lines in grade_parser('tr'):
            if lines.find('th'):
                # is head
                for item in lines.findChildren('th'):
                    grade_head.append(item.text.strip())
            else:
                grade_info.append(dict(map(lambda x,y:(x,y.text.strip()), grade_head, lines.findChildren('td'))))
        return grade_info

    @checkIsLogined
    def get_grade_passed(self):
        jwxt_response = self.session.get( self.jwxt_grade_passed )
        browser_parser = bs4.BeautifulSoup( jwxt_response.content.decode('gbk'), "html.parser" )
        grade_parser = browser_parser.findChildren(name='table' , attrs = {'class':'titleTop2'})
        latest = grade_parser[len(grade_parser)-1].findChild(name='table', attrs = {'class':'displayTag'})
        grade_head = []
        grade_info = []
        for head in latest.findChild(name='thead').findChildren(name='th'):
            grade_head.append(head.text.strip())
        for line in latest.findChild(name='thead').findNextSiblings(name='tr'):
            grade_info.append(dict(map(lambda x,y:(x,y.text.strip()), grade_head, line.findChildren('td'))))
        return grade_info
        
    @checkIsLogined
    def get_grade_failed(self):
        jwxt_response = self.session.get( self.jwxt_grade_failed )
        browser_parser = bs4.BeautifulSoup( jwxt_response.content.decode('gbk'), "html.parser" )
        grade_parser = browser_parser.findChildren(name='table' , attrs = {'class':'titleTop2'})
        latest = grade_parser[0].findChild(name='table', attrs = {'class':'displayTag'})
        grade_head = []
        grade_info = []
        for head in latest.findChild(name='thead').findChildren(name='th'):
            grade_head.append(head.text.strip())
        for line in latest.findChild(name='thead').findNextSiblings(name='tr'):
            grade_info.append(dict(map(lambda x,y:(x,y.text.strip()), grade_head, line.findChildren('td'))))
        return grade_info
