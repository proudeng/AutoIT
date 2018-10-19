from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from mycrypt import prpcrypt
import json
from docutils.parsers.rst.directives import encoding

class browserhandler():
    def __init__(self, webbrowser, cryptkey):
        if webbrowser == "ie":
            self.browser = webdriver.Ie()
        elif webbrowser == "firefox":
            self.browser = webdriver.Firefox()
        elif webbrowser == "chrome":
            self.browser = webdriver.Chrome()

        self.browser.implicitly_wait(10)
        self.pc = prpcrypt(cryptkey)
    
    def reportTime(self, eid, passwd):
        self.browser.get("https://ep.ss.sw.ericsson.se/irj/portal")
        cookies = self.browser.get_cookies()
        print(cookies)
#        cookies = self.browser.get_cookies()
#        print(cookies)

#        cookies = self.browser.get_cookies()
        decryptedPasswd = self.pc.decrypt(passwd)
        eid.encode("utf-8")
        decryptedPasswd.encode("utf-8")
        
        try:
            timeReportPage = self.browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Time Sheet Status'])[1]/following::span[2]")
        except NoSuchElementException :
            usr = self.browser.find_element_by_id("logonuidfield")
            usr.clear()
            usr.send_keys(eid)
            passwd = self.browser.find_element_by_id("logonpassfield")
            passwd.clear()
            passwd.send_keys(decryptedPasswd)
            self.browser.find_element_by_name("uidPasswordLogon").click()
        
            timeReportPage = self.browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Time Sheet Status'])[1]/following::span[2]")
        
        #Enter the time reporting page
        timeReportPage.click()
        
        self.browser.switch_to_frame("contentAreaFrame")
        self.browser.switch_to_frame("isolatedWorkArea")
        
        #find the report plan
        date1_plan = self.browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE1HeaderCaption015")
        date2_plan = self.browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE2HeaderCaption016")
        date3_plan = self.browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE3HeaderCaption017")
        date4_plan = self.browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE4HeaderCaption018")
        date5_plan = self.browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE5HeaderCaption019")
        date6_plan = self.browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE6HeaderCaption020")
        date7_plan = self.browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE7HeaderCaption021")
        
        #update the report with assumption that we fill in the first row
        date1_report = self.browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE1_InputField.0")
        date1_report.click()
        date1_report.clear()
        date1_report.send_keys(date1_plan.text)
        
        date2_report = self.browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE2_InputField.0")
        date2_report.click()
        date2_report.clear()
        date2_report.send_keys(date2_plan.text)
        
        date3_report = self.browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE3_InputField.0")
        date3_report.click()
        date3_report.clear()
        date3_report.send_keys(date3_plan.text)
        
        date4_report = self.browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE4_InputField.0")
        date4_report.click()
        date4_report.clear()
        date4_report.send_keys(date4_plan.text)
        
        date5_report = self.browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE5_InputField.0")
        date5_report.click()
        date5_report.clear()
        date5_report.send_keys(date5_plan.text)
        
        date6_report = self.browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE6_InputField.0")
        date6_report.click()
        date6_report.clear()
        date6_report.send_keys(date6_plan.text)
        
        date7_report = self.browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE7_InputField.0")
        date7_report.click()
        date7_report.clear()
        date7_report.send_keys(date7_plan.text)
#        date7_report.submit()
        
        #save reporting 
#        self.browser.find_element_by_id("aaaaCEAO.LinkBarView.RootUIElementContainer").click()
        self.browser.find_element_by_id("aaaaKEBH.VcCatRecordEntryView.ButtonNext").click()
        self.browser.find_element_by_id("aaaaLBOD.VcGenericButtonView.Save_com_sap_xss_hr_cat_record_vac_review_VcCatRecordReview").click()
        self.browser.switch_to.parent_frame()
        self.browser.switch_to.parent_frame()
        self.browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='My Support'])[1]/following::span[4]").click()
#        self.browser.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='是否确定要注销？'])[1]/following::div[8]").click()
        self.browser.find_element_by_xpath("//*[@id='button_button_std_yes']/tbody/tr/td[2]/div").click()
        self.browser.delete_all_cookies()
        
    
    def __del__(self):
        self.browser.close()
    

if __name__ == '__main__':
    browser = browserhandler("ie", "proudengxiaoshee")
    try:
        fb = open("user.json", 'r')
    except FileNotFoundError:
        print("user configuration file not existing!")
        exit()
    user = json.load(fb)
    for eid in user.keys():
        passwd = user[eid]["passwd"]
        browser.reportTime(eid, passwd)
    exit()
    