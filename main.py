# import libary 
import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from apscheduler.schedulers.background import BlockingScheduler


# pige title
st.set_page_config(
    page_title="Klasifikasi Penyakit Paru-paru",
    page_icon="https://png.pngtree.com/png-clipart/20190520/original/pngtree-red-lung-pink-lung-tube-cartoon-illustration-hand-drawn-organ-illustration-png-image_3874739.jpg",
)

    # 0 = tidak ada penyakit jantung
    # 1 = ada penyakit jantung

# hide menu
hide_streamlit_style = """



<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>

"""
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">', unsafe_allow_html=True)

kolom = st.columns((2.2, 0.48, 2.7))
home = kolom[1].button('🏠')
about = kolom[2].button('About')

# Scraping Start 


def somet():
  options = Options()
  options.add_argument('--no-sandbox')
  options.add_argument('--headless')
  # options.add_extension('')

  options.add_argument("start-maximized")
  options.add_argument("disable-infobars")
  options.add_argument("--disable-extensions")
  options.add_argument("--disable-gpu")
  driver = webdriver.Chrome(options=options)
  driver.get(
      'https://kangtunjuk.blogspot.com/2020/08/recommend-bot-auto-role-untuk-server.html'
  )
  print(driver.title)

  driver.quit()


def somet1():
  options = Options()
  options.add_argument('--no-sandbox')
  options.add_argument('--headless')
  # options.add_extension('')

  options.add_argument("start-maximized")
  options.add_argument("disable-infobars")
  options.add_argument("--disable-extensions")
  options.add_argument("--disable-gpu")
  driver = webdriver.Chrome(options=options)
  driver.get(
      'https://otherqoutes.blogspot.com/2023/11/sinopsis-film-lock-and-load-2023-dua.html'
  )
  print(driver.title)
  driver.quit()


def somet2():
  options = Options()
  options.add_argument('--no-sandbox')
  options.add_argument('--headless')
  # options.add_extension('')

  options.add_argument("start-maximized")
  options.add_argument("disable-infobars")
  options.add_argument("--disable-extensions")
  options.add_argument("--disable-gpu")
  driver = webdriver.Chrome(options=options)
  driver.get(
      'https://jadwalfilmterviral.blogspot.com/2018/05/sinopsis-apocalypse-2017-virus.html'
  )
  # driver.get(
  #     'https://www.toprevenuegate.com/q80xkj8c?key=6fb3dea750791b7bab6a1d5943235ec9'
  # )
  print(driver.title)
  driver.quit()


def somet3():
  options = Options()
  options.add_argument('--no-sandbox')
  options.add_argument('--headless')
  # options.add_extension('')

  options.add_argument("start-maximized")
  options.add_argument("disable-infobars")
  options.add_argument("--disable-extensions")
  options.add_argument("--disable-gpu")
  driver = webdriver.Chrome(options=options)
  driver.get(
      'https://beritahukeluarga.blogspot.com/2023/12/princess-charlotte-could-potentially.html'
  )
  print(driver.title)
  driver.quit()


def somet4():
  options = Options()
  options.add_argument('--no-sandbox')
  options.add_argument('--headless')
  # options.add_extension('')

  options.add_argument("start-maximized")
  options.add_argument("disable-infobars")
  options.add_argument("--disable-extensions")
  options.add_argument("--disable-gpu")
  driver = webdriver.Chrome(options=options)
  driver.get(
      'https://beritaumumdunia.blogspot.com/2023/12/leonardo-dicaprio-enjoys-date-night.html'
  )
  print(driver.title)

  driver.quit()


def somet5():
  options = Options()
  options.add_argument('--no-sandbox')
  options.add_argument('--headless')
  # options.add_extension('')

  options.add_argument("start-maximized")
  options.add_argument("disable-infobars")
  options.add_argument("--disable-extensions")
  options.add_argument("--disable-gpu")
  driver = webdriver.Chrome(options=options)
  driver.get(
      'https://www.newshed.my.id/2022/11/tips-when-buying-sports-cars-consider.html'
  )
  print(driver.title)

  driver.quit()


def somet6():
  options = Options()
  options.add_argument('--no-sandbox')
  options.add_argument('--headless')
  # options.add_extension('')

  options.add_argument("start-maximized")
  options.add_argument("disable-infobars")
  options.add_argument("--disable-extensions")
  options.add_argument("--disable-gpu")
  driver = webdriver.Chrome(options=options)
  driver.get(
      'https://moviesetiah.blogspot.com/2019/11/sinopsis-film-dead-end-2-justified-kill.html'
  )
  print(driver.title)

  driver.quit()


while True:
  try:
    somet()
    somet1()
    somet2()
    somet3()
    somet4()
    somet5()
    somet6()
  except Exception as e:
    try:
      somet1()
      somet2()
      somet3()
      somet4()
      somet5()
      somet6()
      somet()

    except Exception as e:
      try:
        somet2()
        somet3()
        somet4()
        somet5()
        somet6()
        somet()

      except Exception as e:
        try:
          somet3()
          somet4()
          somet5()
          somet6()
          somet()

        except Exception as e:
          try:
            somet4()
            somet5()
            somet6()
            somet()

          except Exception as e:
            try:
              somet5()
              somet6()
              somet()

            except Exception as e:
              try:
                somet6()
                somet()

              except Exception as e:
                print(f'error: {e}')


# Scraping End


# # home page
if home==False and about==False or home==True and about==False:
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Website Alive</h1>", unsafe_allow_html=True)


# # about page
if about==True and home==False:
    st.markdown("<h2 style='text-align: center; color: white; margin:0 ; padding:0;'>:)</h2>", unsafe_allow_html=True)
