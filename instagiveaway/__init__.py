from time import sleep
from selenium import webdriver
from datetime import datetime
import random
import argparse


class InstaGiveaway:
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path="./chromedriver")
        self.username = ''
        self.password = ''
        self.giveaway_posts = []
        self.accounts_to_tag = []

    def __init__(self, username, password, giveaway_posts, accounts_to_tag):
        self.browser = webdriver.Chrome(executable_path="./chromedriver")
        self.username = username
        self.password = password
        self.giveaway_posts = giveaway_posts
        self.accounts_to_tag = accounts_to_tag

    def set_username(username):
        self.username = username

    def set_password(password):
        self.password = password

    def set_giveaway_posts(giveaway_posts):
        self.giveaway_posts = giveaway_posts

    def set_accounts_to_tag(accounts_to_tag):
        self.accounts_to_tag = accounts_to_tag

    def instagram_login(self):
        self.browser.get("https://www.instagram.com")
        self.timeout()

        # Cookies Popup
        accept_cookies = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/div[2]/button[1]')
        accept_cookies.click()

        username_field = self.browser.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password_field = self.browser.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_button = self.browser.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button/div')

        username_field.send_keys(self.username)
        password_field.send_keys(self.password)
        login_button.click()
        self.timeout()

    def navigate_to_post(self, _postId):
        self.browser.get(f'https://www.instagram.com/p/{_postId}/')
        self.timeout()

    def follow_post_user(self):
        follow_button = self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[1]/article/header/div[2]/div[1]/div[2]/button')
        if follow_button.text == "Follow":
            follow_button.click()
        self.timeout()

    def like_post(self):
        heart_svg = self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button/div/span/svg')
        if heart_svg.get_attribute('aria-label') == "Like":
            heart_svg.click()
        self.timeout()

    def comment_on_post(self, _comment_text):
        comment_field = self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
        post_comment_button = self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button')

        comment_field.click()

        # Javascript gets reloaded and we have to redifine the field
        try:
            comment_field.send_keys(_comment_text)
        except:
            comment_field = self.browser.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
            comment_field.send_keys(_comment_text)

        post_comment_button.click()
        self.timeout()

    def get_comment_string(self, number):
        return " ".join(random.choices(self.accounts_to_tag, k=number))

    def get_random_post(self):
        return random.choice(self.giveaway_posts)

    def timeout(self):
        sleep(random.uniform(1, 4))

    def comment_timeout(self):
        sleep(random.uniform(90, 150))

    def run(self, iterations=100, number_of_tags=2):
        print("Logging into Instagram...")
        self.instagram_login()
        i = 0
        print("Commenting on posts...")
        while i < iterations:
            self.navigate_to_post(self.get_random_post())
            self.comment_on_post(self.get_comment_string(number_of_tags))
            self.comment_timeout()
            i += 1
        print("Done!")
