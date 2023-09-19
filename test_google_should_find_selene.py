from selene.support.shared import browser
from selene import be, have


browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element(".LC20lb.MBeuO.DKV0Md").should(have.text('User-oriented Web UI browser tests'))
