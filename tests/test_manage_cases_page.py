#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert

from pages.base_test import BaseTest
from pages.manage_cases_page import MozTrapManageCasesPage


class TestManageCasesPage(BaseTest):

    def test_that_user_can_create_and_delete_case(self, mozwebqa_logged_in):
        manage_cases_pg = MozTrapManageCasesPage(mozwebqa_logged_in)

        case = self.create_case(mozwebqa_logged_in)

        manage_cases_pg.filter_cases_by_name(name=case['name'])

        Assert.true(manage_cases_pg.is_element_present(*case['locator']))

        manage_cases_pg.delete_case(name=case['name'])

        Assert.false(manage_cases_pg.is_element_present(*case['locator']))

        self.delete_product(mozwebqa_logged_in, product=case['product'])
