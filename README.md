![Travis-ci](https://travis-ci.org/champagnepappi/WeConnect.svg)
[![Coverage Status](https://coveralls.io/repos/github/champagnepappi/WeConnect/badge.svg?branch=master)](https://coveralls.io/github/champagnepappi/WeConnect?branch=master)

# WeConnect
WeConnect provides a platform that brings businesses
and individuals together. This platform creates awareness
for businesses and gives the users the ability to write 
reviews about the businesses they have interacted with. 

## Features
- Register
- Login
- Logout
- Password reset
- Register Business
- Update Business
- Delete Business
- Search Business
- Filter searches by location and category

## Getting started
These instructions will get your project up and running for development and testing
purposes
1. Create the virtual environment
   activate the virtual environment `source myenv/bin.activate`

2. Install project dependencies
   You can do this by running `pip -r install requirements.txt`

3. Test the API endpoints by making the following requests
   register user (`/api/v1/auth/register`)
   login user (`/api/v1/auth/login`)
   logout user (`/api/v1/auth/logout`)
   reset user password (`/api/v1/auth/register`)


## How to contribute

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new pull request
