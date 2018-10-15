from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Ie()
browser.get("https://ep.ss.sw.ericsson.se/irj/portal")
browser.implicitly_wait(30)

try:
    timeReportPage = browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Time Sheet Status'])[1]/following::span[2]")
except NoSuchElementException :
    usr = browser.find_element_by_id("logonuidfield")
    usr.clear()
    usr.send_keys("edenjun")
    passwd = browser.find_element_by_id("logonpassfield")
    passwd.clear()
    passwd.send_keys("Storyer1810")
    browser.find_element_by_name("uidPasswordLogon").click()

    timeReportPage = browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Time Sheet Status'])[1]/following::span[2]")

#Enter the time reporting page
timeReportPage.click()

browser.switch_to_frame("contentAreaFrame")
browser.switch_to_frame("isolatedWorkArea")

#find the report plan
date1_plan = browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE1HeaderCaption015")
date2_plan = browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE2HeaderCaption016")
date3_plan = browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE3HeaderCaption017")
date4_plan = browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE4HeaderCaption018")
date5_plan = browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE5HeaderCaption019")
date6_plan = browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE6HeaderCaption020")
date7_plan = browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE7HeaderCaption021")

#update the report with assumption that we fill in the first row
date1_report = browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE1_InputField.0")
date1_report.click()
date1_report.clear()
date1_report.send_keys(date1_plan.text)

date2_report = browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE2_InputField.0")
date2_report.click()
date2_report.clear()
date2_report.send_keys(date2_plan.text)

date3_report = browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE3_InputField.0")
date3_report.click()
date3_report.clear()
date3_report.send_keys(date3_plan.text)

date4_report = browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE4_InputField.0")
date4_report.click()
date4_report.clear()
date4_report.send_keys(date4_plan.text)

date5_report = browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE5_InputField.0")
date5_report.click()
date5_report.clear()
date5_report.send_keys(date5_plan.text)

date6_report = browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE6_InputField.0")
date6_report.click()
date6_report.clear()
date6_report.send_keys(date6_plan.text)

date7_report = browser.find_element_by_id("aaaaKEBH.VcCatTableWeek.WORKDATE7_InputField.0")
date7_report.click()
date7_report.clear()
date7_report.send_keys(date7_plan.text)

#save reporing 
browser.find_element_by_id("aaaaCEAO.LinkBarView.RootUIElementContainer").click()
browser.find_element_by_id("aaaaKEBH.VcCatRecordEntryView.ButtonNext").click()

browser.find_element_by_id("aaaaLBOD.VcGenericButtonView.Save_com_sap_xss_hr_cat_record_vac_review_VcCatRecordReview").click()

class webhandler():
    def __init__(self, browser):
        if browser == "ie":
            webbrowser = webdriver.Ie()
        elif browser == "firefox":
            webbrowser = webdriver.Firefox()
        webbrowser.implicitly_wait(10)
    
    def reportTime(self,eid):
        


if __name__ == '__main__':
    
