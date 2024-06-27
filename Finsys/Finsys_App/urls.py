#Finsys Final
from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    path('',views.Fin_index,name='Fin_index'),
    path('Company_Registration',views.Fin_CompanyReg,name='Fin_CompanyReg'),
    path('Company_Registration2/<id>',views.Fin_CompanyReg2,name='Fin_CompanyReg2'),
    path('Distributor_Registration',views.Fin_DistributorReg,name='Fin_DistributorReg'),
    path('Distributor_Registration_Action',views.Fin_DReg_Action,name='Fin_DReg_Action'),
    path('Distributor_Registration2/<id>',views.Fin_DReg2,name='Fin_DReg2'), 
    path('Distributor_Registration_Action2/<id>',views.Fin_DReg2_Action2,name='Fin_DReg2_Action2'), 
    path('Staff_Registration',views.Fin_StaffReg,name='Fin_StaffReg'),
    path('Adminhome',views.Fin_Adminhome,name='Fin_Adminhome'),
    path('LogIn',views.Fin_login,name='Fin_login'),
    path('Payment_Terms',views.Fin_PaymentTerm,name='Fin_PaymentTerm'),
    path('add_payment_terms',views.Fin_add_payment_terms,name='Fin_add_payment_terms'),
    path('Distributor',views.Fin_ADistributor,name='Fin_ADistributor'),
    path('Distributor_Request',views.Fin_Distributor_Request,name='Fin_Distributor_Request'),
    path('Distributor_Request_overview/<id>',views.Fin_Distributor_Req_overview,name='Fin_Distributor_Req_overview'),
    path('DReq_Accept/<id>',views.Fin_DReq_Accept,name='Fin_DReq_Accept'), 
    path('DReq_Reject/<id>',views.Fin_DReq_Reject,name='Fin_DReq_Reject'),
    path('All_Distributors',views.Fin_All_distributors,name='Fin_All_distributors'),
    path('All_Distributor_Overview/<id>',views.Fin_All_Distributor_Overview,name='Fin_All_Distributor_Overview'),  
    path('Distributor_Home',views.Fin_DHome,name='Fin_DHome'),
    path('companyReg_action',views.Fin_companyReg_action,name='Fin_companyReg_action'),
    path('CompanyReg2_action2/<id>',views.Fin_CompanyReg2_action2,name='Fin_CompanyReg2_action2'),
    path('Fin_Modules/<id>',views.Fin_Modules,name='Fin_Modules'),
    path('Add_Modules/<id>',views.Fin_Add_Modules,name='Fin_Add_Modules'),
    path('Company_Home',views.Fin_Com_Home,name='Fin_Com_Home'),
    path('AClients',views.Fin_AClients,name='Fin_AClients'), 
    path('Fin_AClients_Request',views.Fin_AClients_Request,name='Fin_AClients_Request'),  
    path('Fin_AClients_Request_OverView/<id>',views.Fin_AClients_Request_OverView,name='Fin_AClients_Request_OverView'),
    path('Client_Req_Accept/<id>',views.Fin_Client_Req_Accept,name='Fin_Client_Req_Accept'),
    path('Client_Req_Reject/<id>',views.Fin_Client_Req_Reject,name='Fin_Client_Req_Reject'),
    path('Fin_Admin_clients',views.Fin_Admin_clients,name='Fin_Admin_clients'), 
    path('Fin_Admin_clients_overview/<id>',views.Fin_Admin_clients_overview,name='Fin_Admin_clients_overview'),
    path('LOgout',views.logout,name="logout"),
    path('Company_Profile',views.Fin_Company_Profile,name="Fin_Company_Profile"),
    path('Fin_staffReg_action',views.Fin_staffReg_action,name='Fin_staffReg_action'),
    path('StaffReg2/<id>',views.Fin_StaffReg2,name='Fin_StaffReg2'),
    path('StaffReg2_Action/<id>',views.Fin_StaffReg2_Action,name='Fin_StaffReg2_Action'),
    path('Staff_Req',views.Fin_Staff_Req,name='Fin_Staff_Req'),
    path('Staff_Req_Accept/<id>',views.Fin_Staff_Req_Accept,name='Fin_Staff_Req_Accept'),
    path('Staff_Req_Reject/<id>',views.Fin_Staff_Req_Reject,name='Fin_Staff_Req_Reject'),
    path('All_Staffs',views.Fin_All_Staff,name='Fin_All_Staff'),
    path('DClient_req',views.Fin_DClient_req,name='Fin_DClient_req'),
    path('DClient_Req_Accept/<id>',views.Fin_DClient_Req_Accept,name='Fin_DClient_Req_Accept'),
    path('DClient_Req_Reject/<id>',views.Fin_DClient_Req_Reject,name='Fin_DClient_Req_Reject'), 
    path('DClients',views.Fin_DClients,name='Fin_DClients'),
    path('DProfile',views.Fin_DProfile,name='Fin_DProfile'),
    path('Edit_Modules',views.Fin_Edit_Modules,name='Fin_Edit_Modules'),
    path('Edit_Modules_Action',views.Fin_Edit_Modules_Action,name='Fin_Edit_Modules_Action'),
    path('Anotification',views.Fin_Anotification,name='Fin_Anotification'),
    path('Anoti_Overview/<id>',views.Fin_Anoti_Overview,name='Fin_Anoti_Overview'), 
    path('Module_Updation_Accept/<id>',views.Fin_Module_Updation_Accept,name='Fin_Module_Updation_Accept'),
    path('Module_Updation_Reject/<id>',views.Fin_Module_Updation_Reject,name='Fin_Module_Updation_Reject'),
    path('Change_payment_terms',views.Fin_Change_payment_terms,name='Fin_Change_payment_terms'),
    path('payment_terms_Updation_Accept/<id>',views.Fin_payment_terms_Updation_Accept,name='Fin_payment_terms_Updation_Accept'),
    path('payment_terms_Updation_Reject/<id>',views.Fin_payment_terms_Updation_Reject,name='Fin_payment_terms_Updation_Reject'),
    path('Dnotification',views.Fin_Dnotification,name='Fin_Dnotification'),
    path('Dnoti_Overview/<id>',views.Fin_Dnoti_Overview,name='Fin_Dnoti_Overview'), 
    path('DModule_Updation_Accept/<id>',views.Fin_DModule_Updation_Accept,name='Fin_DModule_Updation_Accept'),
    path('DModule_Updation_Reject/<id>',views.Fin_DModule_Updation_Reject,name='Fin_DModule_Updation_Reject'),
    path('ADpayment_terms_Updation_Accept/<int:id>',views.Fin_ADpayment_terms_Updation_Accept,name='Fin_ADpayment_terms_Updation_Accept'),
    path('ADpayment_terms_Updation_Reject/<int:id>',views.Fin_ADpayment_terms_Updation_Reject,name='Fin_ADpayment_terms_Updation_Reject'),
    path('Cnotification',views.Fin_Cnotification,name='Fin_Cnotification'),
    path('Wrong',views.Fin_Wrong,name='Fin_Wrong'),
    path('Wrong_Action',views.Fin_Wrong_Action,name='Fin_Wrong_Action'),
    path('DChange_payment_terms',views.Fin_DChange_payment_terms,name='Fin_DChange_payment_terms'),
    path('Client_delete/<id>',views.Fin_Client_delete,name='Fin_Client_delete'),
    path('Distributor_delete/<id>',views.Fin_Distributor_delete,name='Fin_Distributor_delete'),
    path('Staff_delete/<id>',views.Fin_Staff_delete,name='Fin_Staff_delete'),
    path('Edit_Company_profile',views.Fin_Edit_Company_profile,name='Fin_Edit_Company_profile'),
    path('Edit_Company_profile_Action',views.Fin_Edit_Company_profile_Action,name='Fin_Edit_Company_profile_Action'),
    path('Edit_Staff_profile',views.Fin_Edit_Staff_profile,name='Fin_Edit_Staff_profile'),
    path('Edit_Staff_profile_Action',views.Fin_Edit_Staff_profile_Action,name='Fin_Edit_Staff_profile_Action'),
    path('Edit_Dprofile',views.Fin_Edit_Dprofile,name='Fin_Edit_Dprofile'),
    path('Edit_Dprofile_Action',views.Fin_Edit_Dprofile_Action,name='Fin_Edit_Dprofile_Action'),
    path('DClient_req_overview/<id>',views.Fin_DClient_req_overview,name='Fin_DClient_req_overview'),
    path('DClients_overview/<id>',views.Fin_DClients_overview,name='Fin_DClients_overview'),
    path('DClient_remove/<id>',views.Fin_DClient_remove,name='Fin_DClient_remove'),
    
    #------shemeem----Items&ChartOfAccounts-----------------------
    # Items
    path('Fin_items',views.Fin_items, name='Fin_items'),
    path('Fin_create_item',views.Fin_createItem, name = 'Fin_createItem'),
    path('Fin_create_new_item',views.Fin_createNewItem, name='Fin_createNewItem'),
    path('Fin_view_item/<int:id>',views.Fin_viewItem, name='Fin_viewItem'),
    path('Fin_save_item_unit',views.Fin_saveItemUnit, name='Fin_saveItemUnit'),
    path('Fin_get_item_units',views.Fin_getItemUnits, name='Fin_getItemUnits'),
    path('Fin_create_new_account_from_items',views.Fin_createNewAccountFromItems, name='Fin_createNewAccountFromItems'),
    path('Fin_change_item_status/<int:id>/<str:status>',views.Fin_changeItemStatus, name='Fin_changeItemStatus'),
    path('Fin_edit_item/<int:id>',views.Fin_editItem, name='Fin_editItem'),
    path('Fin_update_item/<int:id>',views.Fin_updateItem, name='Fin_updateItem'),
    path('Fin_delete_item/<int:id>',views.Fin_deleteItem, name='Fin_deleteItem'),
    path('Fin_item_history/<int:id>',views.Fin_itemHistory, name='Fin_itemHistory'),
    path('Fin_item_transaction_pdf/<int:id>',views.Fin_itemTransactionPdf, name='Fin_itemTransactionPdf'),
    path('Fin_share_item_transactions_to_email/<int:id>',views.Fin_shareItemTransactionsToEmail, name='Fin_shareItemTransactionsToEmail'),
    path('Fin_add_item_comment/<int:id>',views.Fin_addItemComment, name='Fin_addItemComment'),
    path('Fin_delete_item_comment/<int:id>',views.Fin_deleteItemComment, name='Fin_deleteItemComment'),

    # Chart of accounts
    path('Fin_chart_of_accounts',views.Fin_chartOfAccounts, name='Fin_chartOfAccounts'),
    path('Fin_add_account',views.Fin_addAccount, name='Fin_addAccount'),
    path('Fin_check_accounts',views.Fin_checkAccounts, name='Fin_checkAccounts'),
    path('Fin_create_account',views.Fin_createAccount, name='Fin_createAccount'),
    path('Fin_account_overview/<int:id>',views.Fin_accountOverview, name='Fin_accountOverview'),
    path('Fin_change_acc_status/<int:id>/<str:status>',views.Fin_changeAccountStatus, name='Fin_changeAccountStatus'),
    path('Fin_account_transaction_pdf/<int:id>',views.Fin_accountTransactionPdf, name='Fin_accountTransactionPdf'),
    path('Fin_share_acc_transactions_to_email/<int:id>',views.Fin_shareAccountTransactionsToEmail, name='Fin_shareAccountTransactionsToEmail'),
    path('Fin_delete_account/<int:id>',views.Fin_deleteAccount, name= 'Fin_deleteAccount'),
    path('Fin_edit_account/<int:id>',views.Fin_editAccount, name='Fin_editAccount'),
    path('Fin_update_account/<int:id>',views.Fin_updateAccount, name='Fin_updateAccount'),
    path('Fin_account_history/<int:id>',views.Fin_accountHistory, name='Fin_accountHistory'),
    #End
    
    path('Fin_bankholder',views.Fin_bankholder,name='Fin_bankholder'),
    path('Fin_addbank',views.Fin_addbank,name='Fin_addbank'),
    path('Fin_Bankaccountholder',views.Fin_Bankaccountholder,name='Fin_Bankaccountholder'),
    path('Fin_Bankholderview/<int:id>/', views.Fin_Bankholderview, name='Fin_Bankholderview'),
    path('Fin_activebankholder/<int:id>/',views.Fin_activebankholder,name='Fin_activebankholder'),
    path('Fin_inactivatebankaccount/<int:id>/',views.Fin_inactivatebankaccount,name='Fin_inactivatebankaccount'),
    path('Fin_Editholder/<int:id>/',views.Fin_Editholder,name='Fin_Editholder'),
    path('Fin_Editbankholder/<int:id>/',views.Fin_Editbankholder,name='Fin_Editbankholder'),
    path('Fin_deleteholder/<int:id>/',views.Fin_deleteholder,name='Fin_deleteholder'),
    path('Fin_addcomment/<int:id>/', views.Fin_addcomment, name='Fin_addcomment'),
    path('Fin_deletecomment/<int:id>/', views.Fin_deletecomment, name='Fin_deletecomment'),
    path('Fin_Bankhistory/<int:holder_id>/', views.Fin_Bankhistory, name='Fin_Bankhistory'),
    
    path('Fin_fetchaccountnumbers/', views.Fin_fetchaccountnumbers, name='Fin_fetchaccountnumbers'),
    path('Fin_fetchallbanks/', views.Fin_fetchallbanks, name='Fin_fetchallbanks'),
    path('Fin_AddBankinHolder/', views.Fin_AddBankinHolder, name='Fin_AddBankinHolder'),
    
    # -------------Shemeem--------Price List & Customers-------------------------------
    
    path('Fin_price_list',views.Fin_priceList, name='Fin_priceList'),
    path('Fin_add_price_list',views.Fin_addPriceList, name='Fin_addPriceList'),
    path('Fin_create_price_list',views.Fin_createPriceList, name='Fin_createPriceList'),
    path('Fin_view_price_list/<int:id>',views.Fin_viewPriceList, name='Fin_viewPriceList'),
    path('Fin_change_price_list_status/<int:id>/<str:status>',views.Fin_changePriceListStatus, name='Fin_changePriceListStatus'),
    path('Fin_delete_price_list/<int:id>',views.Fin_deletePriceList, name='Fin_deletePriceList'),
    path('Fin_add_price_list_comment/<int:id>',views.Fin_addPriceListComment, name='Fin_addPriceListComment'),
    path('Fin_delete_price_list_comment/<int:id>',views.Fin_deletePriceListComment, name='Fin_deletePriceListComment'),
    path('Fin_price_list_history/<int:id>',views.Fin_priceListHistory, name='Fin_priceListHistory'),
    path('Fin_edit_price_list/<int:id>',views.Fin_editPriceList, name='Fin_editPriceList'),
    path('Fin_update_price_list/<int:id>',views.Fin_updatePriceList, name='Fin_updatePriceList'),
    path('Fin_price_list_view_pdf/<int:id>',views.Fin_priceListViewPdf, name='Fin_priceListViewPdf'),
    path('Fin_share_price_list_view_to_email/<int:id>',views.Fin_sharePriceListViewToEmail, name='Fin_sharePriceListViewToEmail'),
    
    # Customers
    path('Fin_customers',views.Fin_customers, name='Fin_customers'),
    path('Fin_add_customer',views.Fin_addCustomer, name='Fin_addCustomer'),
    path('Fin_check_customer_name',views.Fin_checkCustomerName, name='Fin_checkCustomerName'),
    path('Fin_check_customer_GSTIN',views.Fin_checkCustomerGSTIN, name='Fin_checkCustomerGSTIN'),
    path('Fin_check_customer_PAN',views.Fin_checkCustomerPAN, name='Fin_checkCustomerPAN'),
    path('Fin_check_customer_phone',views.Fin_checkCustomerPhone, name='Fin_checkCustomerPhone'),
    path('Fin_check_customer_email',views.Fin_checkCustomerEmail, name='Fin_checkCustomerEmail'),
    path('Fin_create_customer',views.Fin_createCustomer, name='Fin_createCustomer'),
    path('Fin_new_customer_payment_term',views.Fin_newCustomerPaymentTerm, name='Fin_newCustomerPaymentTerm'),
    path('Fin_view_customer/<int:id>',views.Fin_viewCustomer, name='Fin_viewCustomer'),
    path('Fin_change_customer_status/<int:id>/<str:status>',views.Fin_changeCustomerStatus, name='Fin_changeCustomerStatus'),
    path('Fin_delete_customer/<int:id>',views.Fin_deleteCustomer, name= 'Fin_deleteCustomer'),
    path('Fin_edit_customer/<int:id>',views.Fin_editCustomer, name='Fin_editCustomer'),
    path('Fin_update_customer/<int:id>',views.Fin_updateCustomer, name='Fin_updateCustomer'),
    path('Fin_customer_history/<int:id>',views.Fin_customerHistory, name='Fin_customerHistory'),
    path('Fin_customer_transactions_pdf/<int:id>',views.Fin_customerTransactionsPdf, name='Fin_customerTransactionsPdf'),
    path('Fin_share_customer_transactions_to_email/<int:id>',views.Fin_shareCustomerTransactionsToEmail, name='Fin_shareCustomerTransactionsToEmail'),
    path('Fin_add_customer_comment/<int:id>',views.Fin_addCustomerComment, name='Fin_addCustomerComment'),
    path('Fin_delete_customer_comment/<int:id>',views.Fin_deleteCustomerComment, name='Fin_deleteCustomerComment'),
    
    # harikrishnan (start)--------------------------------
    
    path('employee_list',views.employee_list,name="employee_list"),
    path('employee_create_page',views.employee_create_page,name="employee_create_page"),
    path('employee_save',views.employee_save,name="employee_save"),
    path('employee_overview/<int:pk>',views.employee_overview,name="employee_overview"),
    path('activate/<int:pk>',views.activate,name="activate"),
    path('employee_edit_page/<int:pk>/',views.employee_edit_page,name="employee_edit_page"),
    path('employee_update/<int:pk>',views.employee_update,name="employee_update"),
    path('employee_comment/<int:pk>',views.employee_comment,name="employee_comment"),
    path('employee_comment_view/<int:pk>',views.employee_comment_view,name="employee_comment_view"),
    path('employee_delete/<int:pk>',views.employee_delete,name="employee_delete"),
    path('employee_history/<int:pk>',views.employee_history,name="employee_history"),
    path('employee_profile_email/<int:pk>',views.employee_profile_email,name="employee_profile_email"),
    path('Employee_Profile_PDF/<int:pk>',views.Employee_Profile_PDF,name="Employee_Profile_PDF"),

    path('holiday_list',views.holiday_list,name="holiday_list"),
    path('holiday_create_page',views.holiday_create_page,name="holiday_create_page"),
    path('holiday_add',views.holiday_add,name="holiday_add"),
    path('holiday_calendar_view/<int:mn>/<int:yr>', views.holiday_calendar_view, name='holiday_calendar_view'),
    path('holiday_edit_page/<int:pk>/<int:mn>/<int:yr>', views.holiday_edit_page, name='holiday_edit_page'), 
    path('holiday_update/<int:pk>/<int:mn>/<int:yr>',views.holiday_update,name="holiday_update"),
    path('holiday_delete/<int:pk>',views.holiday_delete,name="holiday_delete"),
    path('holiday_history/<int:month>/<int:year>',views.holiday_history,name="holiday_history"),
    path('employee_overview_print/<int:pk>',views.employee_overview_print,name="employee_overview_print"),
    
    # harikrishnan (end)--------------------------------
    
    # End
    
    # harikrishnan (start)--------------------------------

    path('employee_blood_group',views.employee_blood_group,name="employee_blood_group"),
    path('holiday_comment/<int:mn>/<int:yr>',views.holiday_comment,name="holiday_comment"),
    path('holiday_comment_delete/<int:pk>/<int:mn>/<int:yr>/',views.holiday_comment_delete,name="holiday_comment_delete"),
    path('employee_comment_delete/<int:pk>/<int:id>/',views.employee_comment_delete,name="employee_comment_delete"),
    path('bloodgroup_data',views.bloodgroup_data,name="bloodgroup_data"),
    
    # harikrishnan (end)--------------------------------
    
    # ---------------------------Start Banking------------------------------------ 

    path('Banking_listout',views.Fin_banking_listout,name='Fin_banking_listout'),
    path('Banking_sort_by_balance',views.Fin_banking_sort_by_balance,name='Fin_banking_sort_by_balance'),
    path('Banking_sort_by_name',views.Fin_banking_sort_by_name,name='Fin_banking_sort_by_name'),
    path('Banking_filter_active',views.Fin_banking_filter_active,name='Fin_banking_filter_active'),
    path('Banking_filter_inactive',views.Fin_banking_filter_inactive,name='Fin_banking_filter_inactive'),

    path('Create_bank',views.Fin_create_bank,name='Fin_create_bank'),
    path('Banking_check_account_number',views.Fin_banking_check_account_number,name='Fin_banking_check_account_number'),
    path('Create_bank_account',views.Fin_create_bank_account,name='Fin_create_bank_account'),

    path('View_Bank/<int:id>',views.Fin_view_bank,name='Fin_view_bank'),
    path('Bank_to_cash/<int:id>',views.Fin_bank_to_cash,name='Fin_bank_to_cash'),
    path('Save_bankTocash',views.Fin_save_bankTocash,name='Fin_save_bankTocash'),

    path('Cash_to_bank/<int:id>',views.Fin_cash_to_bank,name='Fin_cash_to_bank'),
    path('Save_cashTobank',views.Fin_save_cashTobank,name='Fin_save_cashTobank'),

    path('Bank_to_bank/<int:id>',views.Fin_bank_to_bank,name='Fin_bank_to_bank'),
    path('Save_bankTobank/<int:id>',views.Fin_save_bankTobank,name='Fin_save_bankTobank'),

    path('Bank_adjust/<int:id>',views.Fin_bank_adjust,name='Fin_bank_adjust'),
    path('Save_bank_adjust',views.Fin_save_bank_adjust,name='Fin_save_bank_adjust'),

    path('Edit_bank/<int:id>',views.Fin_edit_bank,name='Fin_edit_bank'),
    path('Edit_bank_account/<int:id>',views.Fin_edit_bank_account,name='Fin_edit_bank_account'),
    path('Change_bank_status/<int:id>',views.Fin_change_bank_status,name='Fin_change_bank_status'),
    path('Delete_bank/<int:id>',views.Fin_delete_bank,name='Fin_delete_bank'),

    path('Banking_add_file/<int:id>',views.Fin_banking_add_file,name='Fin_banking_add_file'),
    path('Banking_add_comment/<int:id>',views.Fin_banking_add_comment,name='Fin_banking_add_comment'),
    path('Banking_delete_comment/<int:id>',views.Fin_banking_delete_comment,name='Fin_banking_delete_comment'),
    path('Banking_history/<int:id>',views.Fin_banking_history,name='Fin_banking_history'),
    path('ShareBankingStatementToEmail/<int:id>',views.Fin_shareBankingStatementToEmail,name='Fin_shareBankingStatementToEmail'),
    path('Render_pdfstatment_view/<int:id>',views.Fin_render_pdfstatment_view,name='Fin_render_pdfstatment_view'),
    #End    
    
    # -------------Shemeem--------Invoice & Vendors-------------------------------
    # Invoice

    path('Fin_invoice',views.Fin_invoice, name='Fin_invoice'),
    path('Fin_add_invoice',views.Fin_addInvoice, name='Fin_addInvoice'),
    path('Fin_get_bank_account',views.Fin_getBankAccount, name='Fin_getBankAccount'),
    path('Fin_get_invoice_customer_data',views.Fin_getInvoiceCustomerData, name='Fin_getInvoiceCustomerData'),
    path('Fin_check_invoice_number',views.Fin_checkInvoiceNumber, name='Fin_checkInvoiceNumber'),
    path('Fin_get_inv_item_details',views.Fin_getInvItemDetails, name='Fin_getInvItemDetails'),
    path('Fin_create_invoice',views.Fin_createInvoice, name='Fin_createInvoice'),
    path('Fin_view_invoice/<int:id>',views.Fin_viewInvoice, name='Fin_viewInvoice'),
    path('Fin_convert_invoice/<int:id>',views.Fin_convertInvoice, name='Fin_convertInvoice'),
    path('Fin_add_invoice_comment/<int:id>',views.Fin_addInvoiceComment, name='Fin_addInvoiceComment'),
    path('Fin_delete_invoice_comment/<int:id>',views.Fin_deleteInvoiceComment, name='Fin_deleteInvoiceComment'),
    path('Fin_invoice_history/<int:id>',views.Fin_invoiceHistory, name='Fin_invoiceHistory'),
    path('Fin_delete_invoice/<int:id>',views.Fin_deleteInvoice, name= 'Fin_deleteInvoice'),
    path('Fin_invoicePdf/<int:id>',views.Fin_invoicePdf, name='Fin_invoicePdf'),
    path('Fin_share_invoice_to_email/<int:id>',views.Fin_shareInvoiceToEmail, name='Fin_shareInvoiceToEmail'),
    path('Fin_create_invoice_customer',views.Fin_createInvoiceCustomer, name='Fin_createInvoiceCustomer'),
    path('Fin_get_customers',views.Fin_getCustomers, name='Fin_getCustomers'),
    path('Fin_create_invoice_item',views.Fin_createInvoiceItem, name='Fin_createInvoiceItem'),
    path('Fin_get_items',views.Fin_getItems, name='Fin_getItems'),
    path('Fin_edit_invoice/<int:id>',views.Fin_editInvoice, name='Fin_editInvoice'),
    path('Fin_update_invoice/<int:id>',views.Fin_updateInvoice, name='Fin_updateInvoice'),

    # Vendor
    
    path('Fin_vendors',views.Fin_vendors, name='Fin_vendors'),
    path('Fin_add_vendor',views.Fin_addVendor, name='Fin_addVendor'),
    path('Fin_check_vendor_name',views.Fin_checkVendorName, name='Fin_checkVendorName'),
    path('Fin_check_vendor_GSTIN',views.Fin_checkVendorGSTIN, name='Fin_checkVendorGSTIN'),
    path('Fin_check_vendor_PAN',views.Fin_checkVendorPAN, name='Fin_checkVendorPAN'),
    path('Fin_check_vendor_phone',views.Fin_checkVendorPhone, name='Fin_checkVendorPhone'),
    path('Fin_check_vendor_email',views.Fin_checkVendorEmail, name='Fin_checkVendorEmail'),
    path('Fin_create_vendor',views.Fin_createVendor, name='Fin_createVendor'),
    path('Fin_view_vendor/<int:id>',views.Fin_viewVendor, name='Fin_viewVendor'),
    path('Fin_change_vendor_status/<int:id>/<str:status>',views.Fin_changeVendorStatus, name='Fin_changeVendorStatus'),
    path('Fin_delete_vendor/<int:id>',views.Fin_deleteVendor, name= 'Fin_deleteVendor'),
    path('Fin_edit_vendor/<int:id>',views.Fin_editVendor, name='Fin_editVendor'),
    path('Fin_vendor_history/<int:id>',views.Fin_vendorHistory, name='Fin_vendorHistory'),
    path('Fin_add_vendor_comment/<int:id>',views.Fin_addVendorComment, name='Fin_addVendorComment'),
    path('Fin_delete_vendor_comment/<int:id>',views.Fin_deleteVendorComment, name='Fin_deleteVendorComment'),
    path('Fin_vendor_transactions_pdf/<int:id>',views.Fin_vendorTransactionsPdf, name='Fin_vendorTransactionsPdf'),
    path('Fin_share_vendor_transactions_to_email/<int:id>',views.Fin_shareVendorTransactionsToEmail, name='Fin_shareVendorTransactionsToEmail'),
    path('Fin_update_vendor/<int:id>',views.Fin_updateVendor, name='Fin_updateVendor'),
    # End
    
    # -------------Shemeem--------Sales Order-------------------------------
    path('Fin_sales_orders',views.Fin_salesOrder, name='Fin_salesOrder'),
    path('Fin_add_sales_order',views.Fin_addSalesOrder, name='Fin_addSalesOrder'),
    path('Fin_create_sales_order',views.Fin_createSalesOrder, name='Fin_createSalesOrder'),
    path('Fin_check_sales_order_number',views.Fin_checkSalesOrderNumber, name='Fin_checkSalesOrderNumber'),
    path('Fin_view_sales_order/<int:id>',views.Fin_viewSalesOrder, name='Fin_viewSalesOrder'),
    path('Fin_edit_sales_order/<int:id>',views.Fin_editSalesOrder, name='Fin_editSalesOrder'),
    path('Fin_update_sales_order/<int:id>',views.Fin_updateSalesOrder, name='Fin_updateSalesOrder'),
    path('Fin_convert_sales_order/<int:id>',views.Fin_convertSalesOrder, name='Fin_convertSalesOrder'),
    path('Fin_add_sales_order_comment/<int:id>',views.Fin_addSalesOrderComment, name='Fin_addSalesOrderComment'),
    path('Fin_delete_sales_order_comment/<int:id>',views.Fin_deleteSalesOrderComment, name='Fin_deleteSalesOrderComment'),
    path('Fin_sales_order_history/<int:id>',views.Fin_salesOrderHistory, name='Fin_salesOrderHistory'),
    path('Fin_delete_sales_order/<int:id>',views.Fin_deleteSalesOrder, name= 'Fin_deleteSalesOrder'),
    path('Fin_attach_sales_order_file/<int:id>',views.Fin_attachSalesOrderFile, name='Fin_attachSalesOrderFile'),
    path('Fin_sales_order_pdf/<int:id>',views.Fin_salesOrderPdf, name='Fin_salesOrderPdf'),
    path('Fin_share_sales_order_to_email/<int:id>',views.Fin_shareSalesOrderToEmail, name='Fin_shareSalesOrderToEmail'),
    path('Fin_convert_sales_order_to_invoice/<int:id>',views.Fin_convertSalesOrderToInvoice, name='Fin_convertSalesOrderToInvoice'),
    path('Fin_sales_order_convert_invoice/<int:id>',views.Fin_salesOrderConvertInvoice, name='Fin_salesOrderConvertInvoice'),
    path('Fin_convert_sales_order_to_rec_invoice/<int:id>',views.Fin_convertSalesOrderToRecInvoice, name='Fin_convertSalesOrderToRecInvoice'),
    path('Fin_sales_order_convert_rec_invoice/<int:id>',views.Fin_salesOrderConvertRecInvoice, name='Fin_salesOrderConvertRecInvoice'),
    # End
    
    #  ----------------------------- TINTO urls LOAN  sTART-----------------------------

    path('employee_loan_list',views.employee_loan_list,name="employee_loan_list"),
    path('employee_loan_sort_by_employeename',views.employee_loan_sort_by_employeename,name="employee_loan_sort_by_employeename"),
    path('employee_loan_sort_by_balance',views.employee_loan_sort_by_balance,name="employee_loan_sort_by_balance"),
    path('employee_loan_filter_by_active',views.employee_loan_filter_by_active,name="employee_loan_filter_by_active"),
    path('employee_loan_filter_by_inactive',views.employee_loan_filter_by_inactive,name="employee_loan_filter_by_inactive"),
    path('employee_loan_create_page',views.employee_loan_create_page,name="employee_loan_create_page"),
    path('employeedata', views.employeedata, name='employeedata'),
    path('employee_loan_save', views.employee_loan_save, name='employee_loan_save'),
    path('emploanoverview/<int:pk>',views.emploanoverview,name='emploanoverview'),
    path('emploanedit/<int:pk>',views.emploanedit,name='emploanedit'),
    path('emploanrepayment/<int:pk>',views.emploanrepayment,name='emploanrepayment'),
    path('emploanrepaymentsave/<int:pk>',views.emploanrepaymentsave,name='emploanrepaymentsave'),
    path('emploanrepaymentedit/<int:pk>',views.emploanrepaymentedit,name='emploanrepaymentedit'),
    path('emploanaddtional/<int:pk>',views.emploanaddtional,name='emploanaddtional'),
    path('emploanadditionalsave/<int:pk>',views.emploanadditionalsave,name='emploanadditionalsave'),
    path('emploanadditionedit/<int:pk>',views.emploanadditionedit,name='emploanadditionedit'),
    path('addemp', views.addemp, name='addemp'),
    path('add_term', views.add_term, name='add_term'),
    path('term_dropdown', views.term_dropdown, name='term_dropdown'),
    path('emp_dropdown', views.emp_dropdown, name='emp_dropdown'),
    path('laon_status_edit/<int:pk>',views.laon_status_edit,name='laon_status_edit'),
    path('add_loan_comment/<int:pk>',views.add_loan_comment,name='add_loan_comment'),
    path('delete_loan_comment/<int:ph>/<int:pr>',views.delete_loan_comment,name='delete_loan_comment'),
    path('attach_loan_file/<int:pk>',views.attach_loan_file,name='attach_loan_file'),
    path('delete_loan/<int:pk>',views.delete_loan,name='delete_loan'),
    path('shareloanToEmail/<int:pk>',views.shareloanToEmail,name='shareloanToEmail'),
    path('termdata', views.termdata, name='termdata'),
    path('bankdata', views.bankdata, name='bankdata'),
    path('get_repayment_data',views.get_repayment_data,name='get_repayment_data'),
    path('get_addition_data',views.get_addition_data,name='get_addition_data'),
    path('delete_loan_repayment/<int:pk>',views.delete_loan_repayment,name='delete_loan_repayment'),
    path('delete_loan_additional/<int:pk>',views.delete_loan_additional,name='delete_loan_additional'),
 #  ----------------------------- TINTO urls LOAN  END-----------------------------
 
    # CREATED BY AISWARYA
    path('Fin_Eway_bills',views.Fin_Eway_bills, name='Fin_Eway_bills'),
    path('Fin_load_CreateEwaybill',views.Fin_load_CreateEwaybill, name='Fin_load_CreateEwaybill'),
    path('Fin_CreateEwaybill',views.Fin_CreateEwaybill, name='Fin_CreateEwaybill'),
    path('Fin_getEwayCustomerData',views.Fin_getEwayCustomerData, name='Fin_getEwayCustomerData'),
    path('Fin_checkEwayNumber',views.Fin_checkEwayNumber, name='Fin_checkEwayNumber'),
    path('Fin_getEwayItemDetails',views.Fin_getEwayItemDetails, name='Fin_getEwayItemDetails'),
    path('Fin_createEwayCustomer',views.Fin_createEwayCustomer, name='Fin_createEwayCustomer'),
    path('Fin_getEwayCustomers',views.Fin_getEwayCustomers, name='Fin_getEwayCustomers'),
    path('Fin_createEwayItem',views.Fin_createEwayItem, name='Fin_createEwayItem'),
    path('Fin_getEwayItems',views.Fin_getEwayItems, name='Fin_getEwayItems'),
    path('Fin_new_transport_mode',views.Fin_new_transport_mode, name='Fin_new_transport_mode'),
    path('Fin_get_transport_data',views.Fin_get_transport_data, name='Fin_get_transport_data'),
    path('Fin_transportation_modes',views.Fin_transportation_modes, name='Fin_transportation_modes'),
    path('Fin_EwayOverview/<int:id>/',views.Fin_EwayOverview, name='Fin_EwayOverview'),
    path('Fin_EwayPdf/<int:id>',views.Fin_EwayPdf, name='Fin_EwayPdf'),
    path('Fin_shareEwayToEmail/<int:id>',views.Fin_shareEwayToEmail, name='Fin_shareEwayToEmail'),
    path('Fin_EwayDelete/<int:id>',views.Fin_EwayDelete, name='Fin_EwayDelete'),
    path('Fin_EwayHistory/<int:id>',views.Fin_EwayHistory, name='Fin_EwayHistory'),
    path('Fin_EditEway/<int:id>',views.Fin_EditEway, name='Fin_EditEway'),
    path('Fin_EditEwaybills/<int:id>',views.Fin_EditEwaybills, name='Fin_EditEwaybills'),
    path('Fin_EwayConvert/<int:id>',views.Fin_EwayConvert, name='Fin_EwayConvert'),
    #End
             
    #---------------------------- Purchase Bill --------------------------------#

    path('Purchase_Bill_List/',views.Fin_List_Purchase_Bill,name='Fin_List_Purchase_Bill'),
    path('Purchase_Bill_Add/',views.Fin_List_Purchase_Add,name='Fin_List_Purchase_Add'),
    path('Price_List_Data/',views.Fin_Price_List_Data,name='Fin_Price_List_Data'),
    path('Purchase_Bill_Create/',views.Fin_Create_Purchase_Bill,name='Fin_Create_Purchase_Bill'),
    path('Purchase_Bill_No_Check/',views.Fin_Check_Pbill_No,name='Fin_Check_Pbill_No'),
    path('Purchase_Bill_Vendor/',views.Fin_New_Vendor,name='Fin_New_Vendor'),
    path('Purchase_Bill_Customer/',views.Fin_New_Customer,name='Fin_New_Customer'),
    path('Purchase_Bill_Payment_Term/',views.Fin_New_Payment_Term,name='Fin_New_Payment_Term'),
    path('Purchase_Bill_Check_Item_Name/',views.Fin_Check_New_Item_Name,name='Fin_Check_New_Item_Name'),
    path('Purchase_Bill_Check_Item_HSN/',views.Fin_Check_New_Item_HSN,name='Fin_Check_New_Item_HSN'),
    path('Purchase_Bill_Item/',views.Fin_New_Item,name='Fin_New_Item'),
    path('Purchase_Bill_View/<int:id>',views.Fin_View_Purchase_Bill,name='Fin_View_Purchase_Bill'),
    path('Purchase_Bill_Edit/<int:id>',views.Fin_Purchase_Bill_Edit,name='Fin_Purchase_Bill_Edit'),
    path('Purchase_Bill_Update/<int:id>',views.Fin_Update_Purchase_Bill,name='Fin_Update_Purchase_Bill'),
    path('Purchase_Bill_Comment_Create/<int:id>',views.Fin_Purchase_Bill_Add_Edit_Comment,name='Fin_Purchase_Bill_Add_Edit_Comment'),
    path('Purchase_Bill_Comment_Delete/<int:id>',views.Fin_Purchase_Bill_Delete_Comment,name='Fin_Purchase_Bill_Delete_Comment'),
    path('Purchase_Bill_Delete/<int:id>',views.Fin_Delete_Purchase_Bill,name='Fin_Delete_Purchase_Bill'),
    path('Purchase_Bill_Add_File/<int:id>',views.Fin_Add_Additional_Files,name='Fin_Add_Additional_Files'),
    path('Purchase_Bill_History/<int:id>',views.Fin_Purchase_List_History,name='Fin_Purchase_List_History'),
    path('Purchase_Bill_Convert/<int:id>',views.Fin_Convert_To_Active,name='Fin_Convert_To_Active'),
    
    #End
    
    # ---------------Admin updates----------------
    path('remove_payment_terms/<int:pk>',views.Fin_remove_payment_terms,name='Fin_remove_payment_terms'),
    path('Clients_under_Distributors',views.Fin_Clients_under_distributors,name='Fin_Clients_under_distributors'),
    path('getClients_Under_Distributor',views.get_clients_under_distributor,name='get_clients_under_distributor'),
    path('Distributor/client/details/<int:pk>',views.distributor_client_profile_details,name='distributor_client_profile_details'),
    path('Admin/Trial_Period/Section',views.Fin_Admin_trial_period_section,name='Fin_Admin_trial_period_section'),
    path('Admin/Trial_Period/Clients',views.Fin_Admin_trial_period_clients,name='Fin_Admin_trial_period_clients'),
    path('Admin/Trial_Period/Distributor-Clients',views.Fin_Admin_trial_period_distributor_clients,name='Fin_Admin_trial_period_distributor_clients'),
    
    # ---------------Distributor updates----------------
    path('DClient/Trial_Period/Details',views.Fin_trial_periodclients,name='Fin_trial_periodclients'),
    path('Dpayment_terms_Updation_Accept/<int:id>',views.Fin_Dpayment_terms_Updation_Accept,name='Fin_Dpayment_terms_Updation_Accept'),
    path('Dpayment_terms_Updation_Reject/<int:id>',views.Fin_Dpayment_terms_Updation_Reject,name='Fin_Dpayment_terms_Updation_Reject'),
 
    # ---------------Company updates----------------
    path('Company/Trial/Review',views.Fin_company_trial_feedback,name='Fin_company_trial_feedback'),
    #End
    
    # -------------Shemeem--------Estimate-------------------------------
    path('Fin_estimates',views.Fin_estimates, name='Fin_estimates'),
    path('Fin_add_estimate',views.Fin_addEstimate, name='Fin_addEstimate'),
    path('Fin_create_estimate',views.Fin_createEstimate, name='Fin_createEstimate'),
    path('Fin_check_estimate_number',views.Fin_checkEstimateNumber, name='Fin_checkEstimateNumber'),
    path('Fin_view_estimate/<int:id>',views.Fin_viewEstimate, name='Fin_viewEstimate'),
    path('Fin_edit_estimate/<int:id>',views.Fin_editEstimate, name='Fin_editEstimate'),
    path('Fin_update_estimate/<int:id>',views.Fin_updateEstimate, name='Fin_updateEstimate'),
    path('Fin_convert_estimate/<int:id>',views.Fin_convertEstimate, name='Fin_convertEstimate'),
    path('Fin_add_estimate_comment/<int:id>',views.Fin_addEstimateComment, name='Fin_addEstimateComment'),
    path('Fin_delete_estimate_comment/<int:id>',views.Fin_deleteEstimateComment, name='Fin_deleteEstimateComment'),
    path('Fin_estimate_history/<int:id>',views.Fin_estimateHistory, name='Fin_estimateHistory'),
    path('Fin_delete_estimate/<int:id>',views.Fin_deleteEstimate, name= 'Fin_deleteEstimate'),
    path('Fin_estimate_pdf/<int:id>',views.Fin_estimatePdf, name='Fin_estimatePdf'),
    path('Fin_share_estimate_to_email/<int:id>',views.Fin_shareEstimateToEmail, name='Fin_shareEstimateToEmail'),
    path('Fin_attach_estimate_file/<int:id>',views.Fin_attachEstimateFile, name='Fin_attachEstimateFile'),
    path('Fin_convert_estimate_to_invoice/<int:id>',views.Fin_convertEstimateToInvoice, name='Fin_convertEstimateToInvoice'),
    path('Fin_estimate_convert_invoice/<int:id>',views.Fin_estimateConvertInvoice, name='Fin_estimateConvertInvoice'),
    path('Fin_convert_estimate_to_sales_order/<int:id>',views.Fin_convertEstimateToSalesOrder, name='Fin_convertEstimateToSalesOrder'),
    path('Fin_estimate_convert_sales_order/<int:id>',views.Fin_estimateConvertSalesOrder, name='Fin_estimateConvertSalesOrder'),
    path('Fin_convert_estimate_to_recurring_invoice/<int:id>',views.Fin_convertEstimateToRecurringInvoice, name='Fin_convertEstimateToRecurringInvoice'),
    path('Fin_estimate_convert_rec_invoice/<int:id>',views.Fin_estimateConvertRecInvoice, name='Fin_estimateConvertRecInvoice'),
    #End
    
    path('Purchase_Bill_Check_Unit_Name',views.Fin_Check_New_Unit,name='Fin_Check_New_Unit'),
    path('Purchase_Bill_Check_Term',views.Fin_Check_New_Term,name='Fin_Check_New_Term'),
    path('Purchase_Bill_New_Unit',views.Fin_New_Unit,name='Fin_New_Unit'),
    path('Purchase_Bill_Share_Bill/<int:id>',views.Fin_Share_Purchase_Bill,name='Fin_Share_Purchase_Bill'),
    
    path('Purchase_Bill_New_Account',views.Fin_New_Account,name='Fin_New_Account'),
    
    # ---------------Company updates----------------
    path('Company/Profile/Edit/gsttype',views.company_gsttype_change,name='company_gsttype_change'),
    #End
    
    # < ------------- Shemeem -------- > Manual Journals < ------------------------------- >
    path('Fin_manual_journals',views.Fin_manualJournals, name='Fin_manualJournals'),
    path('Fin_add_journal',views.Fin_addJournal, name='Fin_addJournal'),
    path('Fin_check_journal_number',views.Fin_checkJournalNumber, name='Fin_checkJournalNumber'),
    path('Fin_create_journal',views.Fin_createJournal, name='Fin_createJournal'),
    path('Fin_create_new_account_ajax',views.Fin_createNewAccountAjax, name='Fin_createNewAccountAjax'),
    path('Fin_view_journal/<int:id>',views.Fin_viewJournal, name='Fin_viewJournal'),
    path('Fin_edit_journal/<int:id>',views.Fin_editJournal, name='Fin_editJournal'),
    path('Fin_update_journal/<int:id>',views.Fin_updateJournal, name='Fin_updateJournal'),
    path('Fin_convert_journal/<int:id>',views.Fin_convertJournal, name='Fin_convertJournal'),
    path('Fin_add_journal_comment/<int:id>',views.Fin_addJournalComment, name='Fin_addJournalComment'),
    path('Fin_delete_journal_comment/<int:id>',views.Fin_deleteJournalComment, name='Fin_deleteJournalComment'),
    path('Fin_attach_journal_file/<int:id>',views.Fin_attachJournalFile, name='Fin_attachJournalFile'),
    path('Fin_journal_history/<int:id>',views.Fin_journalHistory, name='Fin_journalHistory'),
    path('Fin_delete_journal/<int:id>',views.Fin_deleteJournal, name= 'Fin_deleteJournal'),
    path('Fin_journal_pdf/<int:id>',views.Fin_journalPdf, name='Fin_journalPdf'),
    path('Fin_share_journal_to_email/<int:id>',views.Fin_shareJournalToEmail, name='Fin_shareJournalToEmail'),
    #End
    
    path('Fin_attachEwaybillFile/<int:id>/',views.Fin_attachEwaybillFile, name='Fin_attachEwaybillFile'),
    path('Fin_addEwayComment/<int:id>',views.Fin_addEwayComment, name='Fin_addEwayComment'),
    path('Fin_deleteEwayComment/<int:id>',views.Fin_deleteEwayComment, name='Fin_deleteEwayComment'),
    
    # < ------------- Shemeem -------- > Recurring Invoice < ------------------------------- >
    path('Fin_recurring_invoice',views.Fin_recurringInvoice, name='Fin_recurringInvoice'),
    path('Fin_add_recurring_invoice',views.Fin_addRecurringInvoice, name='Fin_addRecurringInvoice'),
    path('Fin_check_recurring_invoice_number',views.Fin_checkRecurringInvoiceNumber, name='Fin_checkRecurringInvoiceNumber'),
    path('Fin_create_recurring_invoice',views.Fin_createRecurringInvoice, name='Fin_createRecurringInvoice'),
    path('Fin_view_recurring_invoice/<int:id>',views.Fin_viewRecurringInvoice, name='Fin_viewRecurringInvoice'),
    path('Fin_convert_recurring_invoice/<int:id>',views.Fin_convertRecurringInvoice, name='Fin_convertRecurringInvoice'),
    path('Fin_add_recurring_invoice_comment/<int:id>',views.Fin_addRecurringInvoiceComment, name='Fin_addRecurringInvoiceComment'),
    path('Fin_delete_recurring_invoice_comment/<int:id>',views.Fin_deleteRecurringInvoiceComment, name='Fin_deleteRecurringInvoiceComment'),
    path('Fin_recurring_invoice_history/<int:id>',views.Fin_recurringInvoiceHistory, name='Fin_recurringInvoiceHistory'),
    path('Fin_recurring_invoicePdf/<int:id>',views.Fin_recurringInvoicePdf, name='Fin_recurringInvoicePdf'),
    path('Fin_share_recurring_invoice_to_email/<int:id>',views.Fin_shareRecurringInvoiceToEmail, name='Fin_shareRecurringInvoiceToEmail'),
    path('Fin_delete_recurring_invoice/<int:id>',views.Fin_deleteRecurringInvoice, name= 'Fin_deleteRecurringInvoice'),
    path('Fin_new_repeat_every_type',views.Fin_newRepeatEveryType, name='Fin_newRepeatEveryType'),
    path('Fin_edit_recurring_invoice/<int:id>',views.Fin_editRecurringInvoice, name='Fin_editRecurringInvoice'),
    path('Fin_update_recurring_invoice/<int:id>',views.Fin_updateRecurringInvoice, name='Fin_updateRecurringInvoice'),
    
    # End
    path('Fin_Attendance',views.Fin_Attendance,name='Fin_Attendance'),
    path('Fin_Add_Attendance',views.Fin_Add_Attendance,name='Fin_Add_Attendance'),
    path('Fin_Holiday_check_for_attendance',views.Fin_Holiday_check_for_attendance,name='Fin_Holiday_check_for_attendance'),
    path('Fin_attendance_save',views.Fin_attendance_save,name='Fin_attendance_save'),
    path('fin_employee_save_atndnce',views.fin_employee_save_atndnce,name='fin_employee_save_atndnce'),
    path('Fin_Attendanceview/<mn>/<yr>/<id>',views.Fin_Attendanceview,name='Fin_Attendanceview'),
    path('Fin_editAttendance/<id>/<mn>/<yr>/<pk>',views.Fin_editAttendance,name='Fin_editAttendance'),
    path('Fin_deleteAttendance/<id>/<mn>/<yr>/<pk>',views.Fin_deleteAttendance,name='Fin_deleteAttendance'),
    path('Fin_attendance_history/<id>/<mn>/<yr>',views.Fin_attendance_history,name='Fin_attendance_history'),
    path('Fin_addcommentstoleave/<id>/<mn>/<yr>/<pk>',views.Fin_addcommentstoleave,name='Fin_addcommentstoleave'),
    path('Fin_attendancecomments',views.Fin_attendancecomments,name='Fin_attendancecomments'),
    path('Fin_shareLeaveStatementToEmail/<mn>/<yr>/<id>',views.Fin_shareLeaveStatementToEmail,name='Fin_shareLeaveStatementToEmail'),
    
    path('Fin_edit_bank_to_cash/<int:id>',views.Fin_edit_bank_to_cash,name='Fin_edit_bank_to_cash'),
    path('Fin_edit_cash_to_bank/<int:id>',views.Fin_edit_cash_to_bank,name='Fin_edit_cash_to_bank'),
    path('Fin_edit_bank_to_bank/<int:transfer_id>',views.Fin_edit_bank_to_bank,name='Fin_edit_bank_to_bank'),
    path('Fin_edit_bank_adjust/<int:id>',views.Fin_edit_bank_adjust,name='Fin_edit_bank_adjust'),
    path('Fin_edit_bank_trans/<int:id>',views.Fin_edit_bank_trans,name='Fin_edit_bank_trans'),
    path('Fin_bank_transcation_history/<int:id>',views.Fin_bank_transcation_history,name='Fin_bank_transcation_history'),
    path('Fin_bank_transaction_delete/<int:id>',views.Fin_bank_transaction_delete,name='Fin_bank_transaction_delete'),
    
    # < ------------- Shemeem -------- > Purchase Order < ------------------------------- >
    path('Fin_purchase_order',views.Fin_purchaseOrder, name='Fin_purchaseOrder'),
    path('Fin_add_purchase_order',views.Fin_addPurchaseOrder, name='Fin_addPurchaseOrder'),
    path('Fin_check_purchase_order_number',views.Fin_checkPurchaseOrderNumber, name='Fin_checkPurchaseOrderNumber'),
    path('Fin_get_vendor_data',views.Fin_getVendorData, name='Fin_getVendorData'),
    path('Fin_create_purchase_order',views.Fin_createPurchaseOrder, name='Fin_createPurchaseOrder'),
    path('Fin_view_purchase_order/<int:id>',views.Fin_viewPurchaseOrder, name='Fin_viewPurchaseOrder'),
    path('Fin_convert_purchase_order/<int:id>',views.Fin_convertPurchaseOrder, name='Fin_convertPurchaseOrder'),
    path('Fin_add_purchase_order_comment/<int:id>',views.Fin_addPurchaseOrderComment, name='Fin_addPurchaseOrderComment'),
    path('Fin_delete_purchase_order_comment/<int:id>',views.Fin_deletePurchaseOrderComment, name='Fin_deletePurchaseOrderComment'),
    path('Fin_purchase_order_history/<int:id>',views.Fin_purchaseOrderHistory, name='Fin_purchaseOrderHistory'),
    path('Fin_delete_purchase_order/<int:id>',views.Fin_deletePurchaseOrder, name= 'Fin_deletePurchaseOrder'),
    path('Fin_attach_purchase_order_file/<int:id>',views.Fin_attachPurchaseOrderFile, name='Fin_attachPurchaseOrderFile'),
    path('Fin_purchase_order_pdf/<int:id>',views.Fin_purchaseOrderPdf, name='Fin_purchaseOrderPdf'),
    path('Fin_share_purchase_order_to_email/<int:id>',views.Fin_sharePurchaseOrderToEmail, name='Fin_sharePurchaseOrderToEmail'),
    path('Fin_create_vendor_ajax',views.Fin_createVendorAjax, name='Fin_createVendorAjax'),
    path('Fin_get_vendors',views.Fin_getVendors, name='Fin_getVendors'),
    path('Fin_edit_purchase_order/<int:id>',views.Fin_editPurchaseOrder, name='Fin_editPurchaseOrder'),
    path('Fin_update_purchase_order/<int:id>',views.Fin_updatePurchaseOrder, name='Fin_updatePurchaseOrder'),
    path('Fin_convert_purchase_order_to_bill/<int:id>',views.Fin_convertPurchaseOrderToBill, name='Fin_convertPurchaseOrderToBill'),
    path('Fin_purchase_order_convert_bill/<int:id>',views.Fin_purchaseOrderConvertBill, name='Fin_purchaseOrderConvertBill'),
    # End
    path('StockAdjustment',views.StockAdjustment,name='StockAdjustment'),
    path('AddStockAdjustment',views.AddStockAdjustment,name='AddStockAdjustment'),
    path('getitemdata1',views.getitemdata1,name='getitemdata1'),
    path('getitemdata2',views.getitemdata2,name='getitemdata2'),
    path('add_reason',views.add_reason,name='add_reason'),
    path('Stk_adjHistory/<int:id>',views.Stk_adjHistory,name='Stk_adjHistory'),
    path('filterbySave',views.filterbySave,name='filterbySave'),
    path('filterbyDraft',views.filterbyDraft,name='filterbyDraft'),
    path('Fin_StockAdjustmentView',views.Fin_StockAdjustmentView,name='Fin_StockAdjustmentView'),
    path('create_stockadjustment',views.create_stockadjustment,name='create_stockadjustment'),
    path('StockAdjustmentOverview/<int:id>',views.StockAdjustmentOverview,name='StockAdjustmentOverview'),
    path('del_stockadj/<int:id>',views.del_stockadj,name='del_stockadj'),
    path('stockadj_comment/<int:id>',views.stockadj_comment,name='stockadj_comment'),
    path('del_stockcmnt/<int:id>',views.del_stockcmnt,name='del_stockcmnt'),
    path('convert_stockadj/<int:id>',views.convert_stockadj,name='convert_stockadj'),
    path('edit_stockadj/<int:id>',views.edit_stockadj,name='edit_stockadj'),
    path('updatedStockAdj/<int:id>',views.updatedStockAdj,name='updatedStockAdj'),
    path('deleteitem/<int:id>',views.deleteitem,name='deleteitem'),
    path('stock_attachFile/<int:id>',views.stock_attachFile,name='stock_attachFile'),
    path('stockadjToEmail/<int:id>',views.stockadjToEmail,name='stockadjToEmail'),
    
    # 	By tinto mt delivery_challan
    path('deliverylist', views.deliverylist, name='deliverylist'),
    path('newdeliverychallan', views.newdeliverychallan, name='newdeliverychallan'),
    path('createdeliverychallan', views.createdeliverychallan, name='createdeliverychallan'),
    path('Fin_createchallanCustomer',views.Fin_createchallanCustomer, name='Fin_createchallanCustomer'),
    path('Fin_getCustomerschallan',views.Fin_getCustomerschallan, name='Fin_getCustomerschallan'),
    path('customerdata', views.customerdata, name='customerdata'),
    path('challan_overview/<int:id>',views.challan_overview,name='challan_overview'),
    path('editchallan/<int:id>',views.editchallan,name='editchallan'),
    path('Fin_editchallanto/<int:id>',views.Fin_editchallanto,name='Fin_editchallanto'),
    path('Fin_deleteChallan/<int:id>',views.Fin_deleteChallan, name= 'Fin_deleteChallan'),
    path('Fin_addchallanComment/<int:id>',views.Fin_addchallanComment, name= 'Fin_addchallanComment'),
    path('Fin_deletechallanComment/<int:id>',views.Fin_deletechallanComment, name='Fin_deletechallanComment'),
    path('Fin_attachchallanFile/<int:id>',views.Fin_attachchallanFile, name='Fin_attachchallanFile'),
    path('Fin_convertchallan/<int:id>',views.Fin_convertchallan, name='Fin_convertchallan'),
    path('Fin_convertchallanToInvoice/<int:id>',views.Fin_convertchallanToInvoice, name='Fin_convertchallanToInvoice'),
    path('Fin_estimatechallanInvoice/<int:id>',views.Fin_estimatechallanInvoice, name='Fin_estimatechallanInvoice'),
    path('Fin_convertchallanToRecurringInvoice/<int:id>',views.Fin_convertchallanToRecurringInvoice, name='Fin_convertchallanToRecurringInvoice'),
    path('Fin_challanConvertRecInvoice/<int:id>',views.Fin_challanConvertRecInvoice, name='Fin_challanConvertRecInvoice'),
    path('Fin_sharechallanToEmail/<int:id>',views.Fin_sharechallanToEmail, name='Fin_sharechallanToEmail'),
    path('Fin_checkchallanNumber',views.Fin_checkchallanNumber, name='Fin_checkchallanNumber'),
    path('customer_dropdown',views.customer_dropdown, name='customer_dropdown'),
    #End
    
    # < ------------- Shemeem -------- > Expense < ------------------------------- >
    path('Fin_expense',views.Fin_expense, name='Fin_expense'),
    path('Fin_add_expense',views.Fin_addExpense, name='Fin_addExpense'),
    path('Fin_create_new_expense_account',views.Fin_createNewExpenseAccount, name='Fin_createNewExpenseAccount'),
    path('Fin_check_expense_number',views.Fin_checkExpenseNumber, name='Fin_checkExpenseNumber'),
    path('Fin_create_expense',views.Fin_createExpense, name='Fin_createExpense'),
    path('Fin_view_expense/<int:id>',views.Fin_viewExpense, name='Fin_viewExpense'),
    path('Fin_convert_expense/<int:id>',views.Fin_convertExpense, name='Fin_convertExpense'),
    path('Fin_add_expense_comment/<int:id>',views.Fin_addExpenseComment, name='Fin_addExpenseComment'),
    path('Fin_delete_expense_comment/<int:id>',views.Fin_deleteExpenseComment, name='Fin_deleteExpenseComment'),
    path('Fin_expense_history/<int:id>',views.Fin_expenseHistory, name='Fin_expenseHistory'),
    path('Fin_delete_expense/<int:id>',views.Fin_deleteExpense, name= 'Fin_deleteExpense'),
    path('Fin_attach_expense_file/<int:id>',views.Fin_attachExpenseFile, name='Fin_attachExpenseFile'),
    path('Fin_expense_pdf/<int:id>',views.Fin_expensePdf, name='Fin_expensePdf'),
    path('Fin_share_expense_to_email/<int:id>',views.Fin_shareExpenseToEmail, name='Fin_shareExpenseToEmail'),
    path('Fin_edit_expense/<int:id>',views.Fin_editExpense, name='Fin_editExpense'),
    path('Fin_update_expense/<int:id>',views.Fin_updateExpense, name='Fin_updateExpense'),
    path('Fin_check_expense_hsn',views.Fin_checkExpenseHSN, name='Fin_checkExpenseHSN'),
    path('Fin_check_expense_sac',views.Fin_checkExpenseSAC, name='Fin_checkExpenseSAC'),
    # End
    path('Fin_getItems2',views.Fin_getItems2, name='Fin_getItems2'),
    path('Fin_getInvItemDetails2',views.Fin_getInvItemDetails2, name='Fin_getInvItemDetails2'),
    
    path('fin_employee_save_atndnce_EDIT/<mn>/<yr>/<pk>',views.fin_employee_save_atndnce_EDIT,name='fin_employee_save_atndnce_EDIT'),
    path('Fin_editAttendanceVIEW/<mn>/<yr>/<id>/<pk>',views.Fin_editAttendanceVIEW,name='Fin_editAttendanceVIEW'),
    
    #----------------------------start Loan Account------------------------
    
    path('loan_ac_listoutpage',views.loan_ac_listoutpage,name='loan_ac_listoutpage'),
    path('loan_create_page',views.loan_create_page,name='loan_create_page'),
    path('loan_bankdata', views.loan_bankdata, name='loan_bankdata'),
    path('create_loan_ac', views.create_loan_ac, name='create_loan_ac'),
    path('loan_check', views.loan_check, name='loan_check'),
    path('loan_list/<int:id>', views.loan_list, name='loan_list'),
    path('inactive_status/<int:id>', views.inactive_status, name='inactive_status'),
    path('active_status/<int:id>', views.active_status, name='active_status'),
    path('loanaccont_trans/<int:id>', views.loanaccont_trans, name='loanaccont_trans'),
    path('create_loanac_trans/<int:id>', views.create_loanac_trans, name='create_loanac_trans'),
    path('additional_loan_approve/<int:id>', views.additional_loan_approve, name='additional_loan_approve'),
    path('additional_loan_transaction/<int:id>', views.additional_loan_transaction, name='additional_loan_transaction'),
    path('edit_loan_ac_repayment/<int:id>', views.edit_loan_ac_repayment, name='edit_loan_ac_repayment'),
    path('save_edit_loan_repayment/<int:id>', views.save_edit_loan_repayment, name='save_edit_loan_repayment'),
    path('delete_loanac_payment/<int:id>', views.delete_loanac_payment, name='delete_loanac_payment'),
    path('Fin_LoanAccountHistory/<int:id>', views.Fin_LoanAccountHistory, name='Fin_LoanAccountHistory'),
    path('edit_additional_Loan/<int:id>', views.edit_additional_Loan, name='edit_additional_Loan'),
    path('save_edit_additional_loan/<int:id>', views.save_edit_additional_loan, name='save_edit_additional_loan'),
    path('delet_loanaccount/<int:id>', views.delet_loanaccount, name='delet_loanaccount'),
    path('edit_loan_account/<int:id>', views.edit_loan_account, name='edit_loan_account'),
    path('Fin_Share_loanaccount/<int:id>', views.Fin_Share_loanaccount, name='Fin_Share_loanaccount'),
    path('loanac_attachFile/<int:id>', views.loanac_attachFile, name='loanac_attachFile'),
    path('loan_lists_edit/<int:id>', views.loan_lists_edit, name='loan_lists_edit'),
    path('get_loanaddition_data/', views.get_loanaddition_data, name='get_loanaddition_data'),
    path('get_loanrepayment_data/', views.get_loanrepayment_data, name='get_loanrepayment_data'),
    path('save_account',views.save_account,name='save_account'),
    path('loanac_dropdown',views.loanac_dropdown,name='loanac_dropdown'),
    #End
    # url debit note tinto mt
    path('Fin_debitnotelist', views.Fin_debitnotelist, name='Fin_debitnotelist'),
    path('Fin_debitnoteadd', views.Fin_debitnoteadd, name='Fin_debitnoteadd'),
    path('vendordata', views.vendordata, name='vendordata'),
    path('Fin_newdebitnote', views.Fin_newdebitnote, name='Fin_newdebitnote'),
    path('Fin_checkdebitNumber',views.Fin_checkdebitNumber, name='Fin_checkdebitNumber'),
    path('billdata', views.billdata, name='billdata'),
    path('Fin_debit_overview/<int:id>',views.Fin_debit_overview,name='Fin_debit_overview'),
    path('Fin_editdebitnote/<int:id>',views.Fin_editdebitnote,name='Fin_editdebitnote'),
    path('editdebit/<int:id>',views.editdebit,name='editdebit'),
    path('Fin_deletedebit/<int:id>',views.Fin_deletedebit, name= 'Fin_deletedebit'),
    path('Fin_adddebitComment/<int:id>',views.Fin_adddebitComment, name= 'Fin_adddebitComment'),
    path('Fin_deletedebitComment/<int:id>',views.Fin_deletedebitComment, name='Fin_deletedebitComment'),
    path('Fin_attachdebitFile/<int:id>',views.Fin_attachdebitFile, name='Fin_attachdebitFile'),
    path('Fin_sharedebitToEmail/<int:id>',views.Fin_sharedebitToEmail, name='Fin_sharedebitToEmail'),
    path('Fin_convertdebit/<int:id>',views.Fin_convertdebit, name='Fin_convertdebit'),
    path('checkitem', views.checkitem, name='checkitem'),
    #End
    
    # harikrishnan---------------------
    path('Fin_createVendor_modal',views.Fin_createVendor_modal,name='Fin_createVendor_modal'),
    path('Fin_createCustomer_modal',views.Fin_createCustomer_modal,name='Fin_createCustomer_modal'),
    path('Fin_createNewItem_modal',views.Fin_createNewItem_modal,name='Fin_createNewItem_modal'),
    path('Fin_unit_reload_modal/',views.Fin_unit_reload_modal,name='Fin_unit_reload_modal'),
    path('Fin_new_unit_modal/',views.Fin_new_unit_modal,name='Fin_new_unit_modal'),
    path('Fin_new_payment_terms_recurring',views.Fin_new_payment_terms_recurring,name='Fin_new_payment_terms_recurring'),
    path('Fin_saveItemUnit_modal',views.Fin_saveItemUnit_modal,name='Fin_saveItemUnit_modal'),
    path('Fin_recurring_bill_list',views.Fin_recurring_bill_list,name="Fin_recurring_bill_list"),
    path('Fin_recurring_bill_create_page',views.Fin_recurring_bill_create_page,name="Fin_recurring_bill_create_page"),
    path('Fin_recurring_bill_overview/<int:pk>/',views.Fin_recurring_bill_overview,name="Fin_recurring_bill_overview"),
    path('Fin_recurring_bill_save',views.Fin_recurring_bill_save,name="Fin_recurring_bill_save"),
    path('Fin_get_vendor_details/<int:vendor_id>/',views.Fin_get_vendor_details,name='Fin_get_vendor_details'),
    path('Fin_get_customer_details/<int:customer_id>/',views.Fin_get_customer_details,name='Fin_get_customer_details'),
    path('Fin_get_item_details/<int:item_id>/',views.Fin_get_item_details,name='Fin_get_item_details'),
    path('Fin_check_recurring_bill_number',views.Fin_check_recurring_bill_number,name='Fin_check_recurring_bill_number'),
    path('Fin_recurring_bill_delete/<int:pk>',views.Fin_recurring_bill_delete,name="Fin_recurring_bill_delete"),
    path('Fin_recurring_bill_attach_file/<int:pk>/', views.Fin_recurring_bill_attach_file, name='Fin_recurring_bill_attach_file'),
    path('Fin_recurring_bill_edit_page/<int:pk>/',views.Fin_recurring_bill_edit_page,name="Fin_recurring_bill_edit_page"),
    path('Fin_recurring_bill_edit_save/<int:pk>/',views.Fin_recurring_bill_edit_save,name="Fin_recurring_bill_edit_save"),
    path('Fin_end_date',views.Fin_end_date,name="Fin_end_date"),
    path('Fin_recurring_bill_email',views.Fin_recurring_bill_email,name="Fin_recurring_bill_email"),
    path('Fin_recurring_bill_comment',views.Fin_recurring_bill_comment,name='Fin_recurring_bill_comment'),
    path('Fin_recurring_bill_comment_delete/<int:pk>/<int:id>/',views.Fin_recurring_bill_comment_delete,name='Fin_recurring_bill_comment_delete'),
    path('Fin_recurring_bill_history/<int:pk>',views.Fin_recurring_bill_history,name='Fin_recurring_bill_history'),
    path('Fin_recurring_bill_convert/<int:pk>',views.Fin_recurring_bill_convert,name='Fin_recurring_bill_convert'),
    path('Fin_recurring_bill_usercheck',views.Fin_recurring_bill_usercheck,name='Fin_recurring_bill_usercheck'),
    path('Fin_shareRBToEmail/<int:id>',views.Fin_shareRBToEmail,name='Fin_shareRBToEmail'),
    path('Fin_check_recurring_bill_number_editpage/<int:pk>',views.Fin_check_recurring_bill_number_editpage,name='Fin_check_recurring_bill_number_editpage'),
    path('Fin_get_bank_details/<str:bankNum>',views.Fin_get_bank_details,name="Fin_get_bank_details"),
    path('Fin_check_hsn_RB',views.Fin_check_hsn_RB,name="Fin_check_hsn_RB"),
    path('Fin_get_pricelist_details/<int:price_id>/<int:items_id>/',views.Fin_get_pricelist_details,name='Fin_get_pricelist_details'),
    # harikrishnankb end ------------
    path('loan_bankdata_repayment',views.loan_bankdata_repayment,name='loan_bankdata_repayment'),
    
    # ...............Payement Recevied.........................Antony.........
    path('Fin_view_payment_received',views.Fin_view_payment_received,name='Fin_view_payment_received'),
    path('Fin_add_payment_received',views.Fin_add_payment_received,name='Fin_add_payment_received'),
    path('Fin_paymentreceivecustomer',views.Fin_paymentreceivecustomer,name='Fin_paymentreceivecustomer'),
    path('Fin_create_receivepayment_customer',views.Fin_create_receivepayment_customer,name='Fin_create_receivepayment_customer'),
    path('Fin_getpaymentreceivecustomers',views.Fin_getpaymentreceivecustomers,name='Fin_getpaymentreceivecustomers'),
    path('Fin_newCustomerPaymentReceivedTerm',views.Fin_newCustomerPaymentReceivedTerm,name='Fin_newCustomerPaymentReceivedTerm'),
    path('Fin_check_paymentreceived_CustomerName',views.Fin_check_paymentreceived_CustomerName,name='Fin_check_paymentreceived_CustomerName'),
    path('Fin_check_paymentreceived_CustomerGSTIN',views.Fin_check_paymentreceived_CustomerGSTIN,name='Fin_check_paymentreceived_CustomerGSTIN'),
    path('Fin_check_paymentreceived_CustomerPAN',views.Fin_check_paymentreceived_CustomerPAN,name='Fin_check_paymentreceived_CustomerPAN'),
    path('Fin_check_paymentreceived_CustomerPhone',views.Fin_check_paymentreceived_CustomerPhone,name='Fin_check_paymentreceived_CustomerPhone'),
    path('Fin_check_paymentreceived_CustomerEmail',views.Fin_check_paymentreceived_CustomerEmail,name='Fin_check_paymentreceived_CustomerEmail'),
    path('Fin_Create_Payment_Received',views.Fin_Create_Payment_Received,name='Fin_Create_Payment_Received'),
    path('Fin_overview_payment_received/<int:id>',views.Fin_overview_payment_received,name='Fin_overview_payment_received'),
    path('Fin_Payment_Received_History/<int:id>',views.Fin_Payment_Received_History,name='Fin_Payment_Received_History'),
    path('Fin_payment_received_Comment/<int:id>',views.Fin_payment_received_Comment,name='Fin_payment_received_Comment'),
    path('Fin_deletePaymentComment/<int:id>',views.Fin_deletePaymentComment,name='Fin_deletePaymentComment'),
    path('Fin_deletePayment/<int:id>',views.Fin_deletePayment,name='Fin_deletePayment'),
    path('Fin_convertpaymentsave/<int:id>',views.Fin_convertpaymentsave,name='Fin_convertpaymentsave'),
    path('Fin_sharePaymentToEmail/<int:id>',views.Fin_sharePaymentToEmail,name='Fin_sharePaymentToEmail'),
    path('fetch_invoice_data',views.fetch_invoice_data,name='fetch_invoice_data'),
    path('get_payemnt_bankacc_num',views.get_payemnt_bankacc_num,name='get_payemnt_bankacc_num'),
    path('Fin_edit_payment_received/<int:id>',views.Fin_edit_payment_received,name='Fin_edit_payment_received'),
    path('Fin_Update_Payment_Received/<int:id>',views.Fin_Update_Payment_Received,name='Fin_Update_Payment_Received'),
    path('payment_add_file/<int:id>',views.payment_add_file,name='payment_add_file'),
    #End
    #------------------Salary Details---------------------------#
    path('Fin_salary_details',views.Fin_salary_details,name='Fin_salary_details'),
    path('sort_employee_name_salary/',views.sort_employee_name_salary, name='sort_employee_name_salary'),
    path('payroll_sort_employeesalary_by_month/',views.payroll_sort_employeesalary_by_month, name='payroll_sort_employeesalary_by_month'),
    path('filter_by_status_save/', views.filter_by_status_save, name='filter_by_status_save'),
    path('filter_by_status_draft/', views.filter_by_status_draft, name='filter_by_status_draft'),
    path('payroll_addsalarydetails/', views.payroll_addsalarydetails, name='payroll_addsalarydetails'),
    path('listemployee_salary',views.listemployee_salary,name='listemployee_salary'),
    path('AddEmployeeInSalaryPage',views.AddEmployeeInSalaryPage,name='AddEmployeeInSalaryPage'),
    path('getDays',views.getDays,name='getDays'),
    path('calculate_salary/', views.calculate_salary, name='calculate_salary'),
    path('item_dropdown', views.item_dropdown, name='item_dropdown'),
    re_path(r'^itemdata$', views.itemdata, name='itemdata'),
    path('Fin_salary_overview/<str:employee_id>/<int:salary_id>/', views.Fin_salary_overview, name='Fin_salary_overview'),
    path('Fin_salarypdf/<int:employee_id>/<int:salary_id>/', views.Fin_salarypdf, name='Fin_salarypdf'),
    path('Fin_shareSalaryToEmail/<int:employee_id>/<int:salary_id>/', views.Fin_shareSalaryToEmail, name='Fin_shareSalaryToEmail'),
    path('Fin_deletesalary/<str:employee_id>/<int:salary_id>/', views.Fin_deletesalary, name='Fin_deletesalary'),
    path('Fin_addEmployeeComment/<int:employee_id>/<int:salary_id>/',views.Fin_addEmployeeComment, name='Fin_addEmployeeComment'),
    path('Fin_deleteEmployeeComment/<int:id>/<int:salary_id>/',views.Fin_deleteEmployeeComment, name='Fin_deleteEmployeeComment'),
    path('Fin_salaryedit/<int:employee_id>/<int:salary_id>/', views.Fin_salaryedit, name ='Fin_salaryedit'),
    path('Fin_SalaryHistory/<int:id>',views.Fin_SalaryHistory, name='Fin_SalaryHistory'),
    path('Fin_salarysave/<int:employee_id>/<int:salary_id>/', views.Fin_salarysave, name ='Fin_salarysave'),
    #-------------------------------------------------End---------------------#
    # ...............Payement Recevied.........................Antony.........
    path('Fin_checkpaymentNumber',views.Fin_checkpaymentNumber,name='Fin_checkpaymentNumber'),
    #End
    path('Fin_paymentmade', views.Fin_paymentmade, name='Fin_paymentmade'),
    path('Fin_addpaymentmade', views.Fin_addpaymentmade, name='Fin_addpaymentmade'),
    path('Fin_PaymentMade_getVendorData', views.Fin_PaymentMade_getVendorData, name='Fin_PaymentMade_getVendorData'),
    path('Fin_checkPaymentMadeNumber', views.Fin_checkPaymentMadeNumber, name='Fin_checkPaymentMadeNumber'),
    
    path('Fin_createPaymentMade', views.Fin_createPaymentMade, name='Fin_createPaymentMade'),
    path('Fin_ViewPaymentMade/<int:id>/', views.Fin_ViewPaymentMade, name='Fin_ViewPaymentMade'),
    path('Fin_convertPaymentMade/<int:id>', views.Fin_convertPaymentMade, name='Fin_convertPaymentMade'),
    path('Fin_addPaymentMadeComment/<int:id>', views.Fin_addPaymentMadeComment, name='Fin_addPaymentMadeComment'),
    path('Fin_deletePaymentMadeComment/<int:id>', views.Fin_deletePaymentMadeComment, name='Fin_deletePaymentMadeComment'),
    path('Fin_PaymentMadeHistory/<int:id>', views.Fin_PaymentMadeHistory, name='Fin_PaymentMadeHistory'),
    path('Fin_deletePaymentMade/<int:id>', views.Fin_deletePaymentMade, name='Fin_deletePaymentMade'),
    path('Fin_attachPaymentMadeFile/<int:id>', views.Fin_attachPaymentMadeFile, name='Fin_attachPaymentMadeFile'),
    path('Fin_PaymentMadePdf/<int:id>', views.Fin_PaymentMadePdf, name='Fin_PaymentMadePdf'),
    path('Fin_sharePaymentMadeToEmail/<int:id>', views.Fin_sharePaymentMadeToEmail, name='Fin_sharePaymentMadeToEmail'),
    path('Fin_PaymentMade_getVendors', views.Fin_PaymentMade_getVendors, name='Fin_PaymentMade_getVendors'),
    path('Fin_PaymentMade_createVendorAjax', views.Fin_PaymentMade_createVendorAjax, name='Fin_PaymentMade_createVendorAjax'),
    path('Fin_EditPaymentMade/<int:id>', views.Fin_EditPaymentMade, name='Fin_EditPaymentMade'),
    path('Fin_UpdatePaymentMade/<int:id>', views.Fin_UpdatePaymentMade, name='Fin_UpdatePaymentMade'),
    path('Fin_SaveBills', views.Fin_SaveBills, name='Fin_SaveBills'),
    path('Fin_VendorPaymentDetails_Edit/', views.Fin_VendorPaymentDetails_Edit, name='Fin_VendorPaymentDetails_Edit'), 
    path('fetch_payments/', views.fetch_payments, name='fetch_payments'),
    
    path('Purchase_Bill_All_Items_Add',views.Fin_Get_All_Items_Add,name='Fin_Get_All_Items_Add'),
    path('Purchase_Bill_All_Items_Edit',views.Fin_Get_All_Items_Edit,name='Fin_Get_All_Items_Edit'),
    
    # < ------------- Shemeem -------- > CASH IN HAND < ------------------------------- >
    path('Fin_cash_in_hand',views.Fin_cashInHand, name='Fin_cashInHand'),
    path('Fin_add_cash',views.Fin_addCash, name='Fin_addCash'),
    path('Fin_save_added_cash',views.Fin_saveAddCash, name='Fin_saveAddCash'),
    path('Fin_edit_added_cash/<int:id>',views.Fin_editAddCash, name='Fin_editAddCash'),
    path('Fin_update_added_cash/<int:id>',views.Fin_updateAddCash, name='Fin_updateAddCash'),
    path('Fin_cash_in_hand_statement',views.Fin_cashInHandStatement, name='Fin_cashInHandStatement'),
    path('Fin_cash_in_hand_statement_pdf',views.Fin_cashInHandStatementPdf, name='Fin_cashInHandStatementPdf'),
    path('Fin_share_cash_in_hand_statement_to_email',views.Fin_shareCashInHandStatementToEmail, name='Fin_shareCashInHandStatementToEmail'),
    path('Fin_cash_in_hand_graph/<str:period>',views.Fin_cashInHandGraph, name='Fin_cashInHandGraph'),
    path('Fin_delete_added_cash/<int:id>',views.Fin_deleteAddedCash, name='Fin_deleteAddedCash'),
    # End
    #------------------Salary Details---------------------------#
    path('check_employee_id/', views.check_employee_id, name='check_employee_id'),
    path('emp_dropdown_active_not', views.emp_dropdown_active_not, name='emp_dropdown_active_not'),
    #-------------------------------------------------End---------------------#
    #Reshna-Retainer_Invoice--------------------------
    path('Fin_RET_INV_Listout',views.Fin_RET_INV_Listout,name='Fin_RET_INV_Listout'),
    path('Fin_Create_RET_INV',views.Fin_Create_RET_INV,name='Fin_Create_RET_INV'),
    path('Fin_RET_INV_Add',views.Fin_RET_INV_Add,name='Fin_RET_INV_Add'),
    path('Fin_get_RET_INV_Customers',views.Fin_get_RET_INV_Customers,name='Fin_get_RET_INV_Customers'),
    path('Fin_RET_INV_Customer',views.Fin_RET_INV_Customer,name='Fin_RET_INV_Customer'),
    path('Fin_Retinvcustomer_paymentterm',views.Fin_Retinvcustomer_paymentterm,name='Fin_Retinvcustomer_paymentterm'),
    path('Fin_RETINV_CustomerData',views.Fin_RETINV_CustomerData,name='Fin_RETINV_CustomerData'),
    path('fetch_bank_account',views.fetch_bank_account,name='fetch_bank_account'),
    path('Fin_validate_retinv_number',views.Fin_validate_retinv_number,name='Fin_validate_retinv_number'),
    path('Fin_RETInvoiceItem',views.Fin_RETInvoiceItem,name='Fin_RETInvoiceItem'),
    path('validate_hsn',views.validate_hsn,name='validate_hsn'),
    path('validate_name',views.validate_name,name='validate_name'),
    path('Fin_Reloaditems',views.Fin_Reloaditems,name='Fin_Reloaditems'),
    path('Fin_RETINVItemDetails',views.Fin_RETINVItemDetails,name='Fin_RETINVItemDetails'),
    path('Fin_RI_Overview/<int:id>',views.Fin_RI_Overview,name='Fin_RI_Overview'),
    path('Fin_deleteRI/<int:id>',views.Fin_deleteRI,name='Fin_deleteRI'),
    path('Fin_addRETINVComment/<int:id>',views.Fin_addRETINVComment,name='Fin_addRETINVComment'),
    path('Fin_deleteRETINVComment/<int:id>',views.Fin_deleteRETINVComment,name='Fin_deleteRETINVComment'),
    path('Fin_RIHistory/<int:id>',views.Fin_RIHistory,name='Fin_RIHistory'),
    path('Fin_deleteRI/<int:id>',views.Fin_deleteRI,name='Fin_deleteRI'),
    path('Fin_RIPdf/<int:id>',views.Fin_RIPdf,name='Fin_RIPdf'),
    path('Fin_shareRIEmail/<int:id>',views.Fin_shareRIEmail,name='Fin_shareRIEmail'),
    path('Fin_RET_INV_edit/<int:id>',views.Fin_RET_INV_edit,name='Fin_RET_INV_edit'),
    path('Fin_RET_INV_update/<int:id>',views.Fin_RET_INV_update,name='Fin_RET_INV_update'),
    path('Fin_convertRI/<int:id>',views.Fin_convertRI,name='Fin_convertRI'),
    #--------------------------------------------------------------------------------
    #------------------Salary Details---------------------------#
    path('Employee-Edit/<int:employee_id>/<int:sal_id>/', views.employee_edit, name='employee_edit'),
    path('Edit_getDays',views.Edit_getDays,name='Edit_getDays'),
    #-------------------------------------------------End---------------------#
    # < ------------- Shemeem -------- > CHEQUES < ------------------------------- >
    path('Fin_cheques',views.Fin_cheques, name='Fin_cheques'),
    path('Fin_cheque_statement',views.Fin_chequeStatement, name='Fin_chequeStatement'),
    path('Fin_cheque_statement_pdf',views.Fin_chequeStatementPdf, name='Fin_chequeStatementPdf'),
    path('Fin_share_cheque_statement_to_email',views.Fin_shareChequeStatementToEmail, name='Fin_shareChequeStatementToEmail'),

    # < ------------- Shemeem -------- > UPI < ------------------------------- >
    path('Fin_upi_payments',views.Fin_upiPayments, name='Fin_upiPayments'),
    path('Fin_upi_statement',views.Fin_upiStatement, name='Fin_upiStatement'),
    path('Fin_upi_statement_pdf',views.Fin_upiStatementPdf, name='Fin_upiStatementPdf'),
    path('Fin_share_upi_statement_to_email',views.Fin_shareUpiStatementToEmail, name='Fin_shareUpiStatementToEmail'),
    # End
    # < ------------- Shemeem -------- > CREDIT NOTES < ------------------------------- >
    path('Fin_credit_notes',views.Fin_creditNotes, name = 'Fin_creditNotes'),
    path('Fin_add_credit_note',views.Fin_addCreditNote, name='Fin_addCreditNote'),
    path('Fin_get_invoice_numbers',views.Fin_getInvoiceNumbers, name='Fin_getInvoiceNumbers'),
    path('Fin_get_invoice_numbers_edit',views.Fin_getInvoiceNumbersEdit, name='Fin_getInvoiceNumbersEdit'),
    path('Fin_get_invoice_details',views.Fin_getInvoiceDet, name='Fin_getInvoiceDet'),
    path('Fin_create_credit_note',views.Fin_createCreditNote, name='Fin_createCreditNote'),
    path('Fin_check_credit_note_number',views.checkCreditNoteNumber, name='checkCreditNoteNumber'),
    path('Fin_view_credit_note/<int:id>',views.Fin_viewCreditNote, name='Fin_viewCreditNote'),
    path('Fin_convert_credit_note/<int:id>',views.Fin_convertCreditNote, name='Fin_convertCreditNote'),
    path('Fin_credit_note_history/<int:id>',views.Fin_creditNoteHistory, name='Fin_creditNoteHistory'),
    path('Fin_add_credit_note_comment/<int:id>',views.Fin_addCreditNoteComment, name='Fin_addCreditNoteComment'),
    path('Fin_delete_credit_note_comment/<int:id>',views.Fin_deleteCreditNoteComment, name='Fin_deleteCreditNoteComment'),
    path('Fin_attach_credit_note_file/<int:id>',views.Fin_attachCreditNoteFile, name='Fin_attachCreditNoteFile'),
    path('Fin_edit_credit_note/<int:id>',views.Fin_editCreditNote, name='Fin_editCreditNote'),
    path('Fin_update_credit_note/<int:id>',views.Fin_updateCreditNote, name='Fin_updateCreditNote'),
    path('Fin_credit_note_pdf/<int:id>',views.Fin_creditNotePdf, name='Fin_creditNotePdf'),
    path('Fin_share_credit_note_to_email/<int:id>',views.Fin_shareCreditNoteToEmail, name='Fin_shareCreditNoteToEmail'),
    path('Fin_delete_credit_note/<int:id>',views.Fin_deleteCreditNote, name= 'Fin_deleteCreditNote'),
    path('Fin_get_inv_paid_amount',views.Fin_getInvoicePaidAmount, name='Fin_getInvoicePaidAmount'),
    # End
    # < ------------- Shemeem -------- > Reports - Sales by Item & Customer < ------------------------------- >
    path('Fin_report_sales_by_customer',views.Fin_salesByCustomerReport, name='Fin_salesByCustomerReport'),
    path('Fin_sales_by_customer_report_customized',views.Fin_salesByCustomerReportCustomized, name='Fin_salesByCustomerReportCustomized'),
    path('Fin_share_sales_by_customer_report_to_email',views.Fin_shareSalesByCustomerReportToEmail, name='Fin_shareSalesByCustomerReportToEmail'),
    path('Fin_report_sales_by_item',views.Fin_salesByItemReport, name='Fin_salesByItemReport'),
    path('Fin_sales_by_items_report_customized',views.Fin_salesByItemsReportCustomized, name='Fin_salesByItemsReportCustomized'),
    path('Fin_share_sales_by_item_report_to_email',views.Fin_shareSalesByItemReportToEmail, name='Fin_shareSalesByItemReportToEmail'),

    # End
    path('Fin_Check_New_Item_SAC',views.Fin_Check_New_Item_SAC, name='Fin_Check_New_Item_SAC'),
    # ------------------------------------ Purchase Report ------------------------------------
    path('Fin_purchase_report_vendor',views.Fin_purchase_report_vendor, name='Fin_purchase_report_vendor'),
    path('Fin_Share_Purchase_Report_Vendor',views.Fin_Share_Purchase_Report_Vendor, name='Fin_Share_Purchase_Report_Vendor'),
    path('Fin_customize_purchase_report_vendor',views.Fin_customize_purchase_report_vendor, name='Fin_customize_purchase_report_vendor'),
    path('Fin_purchase_report_item',views.Fin_purchase_report_item, name='Fin_purchase_report_item'),
    path('Fin_customize_purchase_report_item',views.Fin_customize_purchase_report_item, name='Fin_customize_purchase_report_item'),
    path('Fin_Share_Purchase_Report_Item',views.Fin_Share_Purchase_Report_Item, name='Fin_Share_Purchase_Report_Item'),
    #End
    # < ------------- Shemeem -------- > Reports - DayBook < ------------------------------- >
    path('Fin_report_day_book',views.Fin_dayBookReport, name='Fin_dayBookReport'),
    path('Fin_day_book_report_customized',views.Fin_dayBookReportCustomized, name='Fin_dayBookReportCustomized'),
    path('Fin_share_day_book_report_to_email',views.Fin_shareDayBookReportToEmail, name='Fin_shareDayBookReportToEmail'),
    # End
    # ------------------------------------ customerbalence Report ------------------------------------
    path('Fin_customerbalence',views.Fin_customerbalence, name='Fin_customerbalence'),
    path('Fin_shareCustomerBalenceReportToEmail',views.Fin_shareCustomerBalenceReportToEmail, name='Fin_shareCustomerBalenceReportToEmail'),
    path('Fin_customerbalence_report_customized',views.Fin_customerbalence_report_customized, name='Fin_customerbalence_report_customized'),
    #End
    # < ------------- Haripriya -------- > Reports -Retainer Invoice < ------------------------------- >
    path('Fin_Retainer_Report',views.Fin_Retainer_Report, name='Fin_Retainer_Report'),
    path('Fin_RetainerInvoReportCustomized',views.Fin_RetainerInvoReportCustomized, name='Fin_RetainerInvoReportCustomized'),
    path('Fin_shareRetainerInvoiceReportToEmail',views.Fin_shareRetainerInvoiceReportToEmail, name='Fin_shareRetainerInvoiceReportToEmail'),
    #End
    # < ------------- Shemeem -------- > Reports - Sales Order Details < ------------------------------- >
    path('Fin_report_sales_order_details',views.Fin_salesOrderDetailsReport, name='Fin_salesOrderDetailsReport'),
    path('Fin_sales_order_details_report_customized',views.Fin_salesOrderDetailsCustomized, name='Fin_salesOrderDetailsCustomized'),
    path('Fin_share_sales_order_details_report_to_email',views.Fin_shareSalesOrderDetailsReportToEmail, name='Fin_shareSalesOrderDetailsReportToEmail'),
    # End
    # < ------------- Shemeem -------- > Reports - Purchase Order Details < ------------------------------- >
    path('Fin_report_purchase_order_details',views.Fin_purchaseOrderDetailsReport, name='Fin_purchaseOrderDetailsReport'),
    path('Fin_purchase_order_details_report_customized',views.Fin_purchaseOrderDetailsCustomized, name='Fin_purchaseOrderDetailsCustomized'),
    path('Fin_share_purchase_order_details_report_to_email',views.Fin_sharePurchaseOrderDetailsReportToEmail, name='Fin_sharePurchaseOrderDetailsReportToEmail'),
    # End
    # ------------------------------------ estimate Report ------------------------------------
    path('Fin_estimate_report',views.Fin_estimate_report, name='Fin_estimate_report'),
    path('Fin_estimateDetailsCustomized',views.Fin_estimateDetailsCustomized, name='Fin_estimateDetailsCustomized'),
    path('Fin_shareestimateDetailsReportToEmail',views.Fin_shareestimateDetailsReportToEmail, name='Fin_shareestimateDetailsReportToEmail'),
    #End
    # ------------------------------------ rec invoice Report ------------------------------------
    path('Fin_recInvoice_report',views.Fin_recInvoice_report, name='Fin_recInvoice_report'),
    path('Fin_recinvCustomized',views.Fin_recinvCustomized, name='Fin_recinvCustomized'),
    path('Fin_shareREC_INVOICEDetailsReportToEmail',views.Fin_shareREC_INVOICEDetailsReportToEmail, name='Fin_shareREC_INVOICEDetailsReportToEmail'),
    #End
    # ------------------------------------ Aging Summary ------------------------------------
    path('Fin_aging_summary',views.Fin_aging_summary, name='Fin_aging_summary'),
    path('Fin_customize_aging_summary',views.Fin_customize_aging_summary, name='Fin_customize_aging_summary'),
    path('Fin_Share_Aging_Summary',views.Fin_Share_Aging_Summary, name='Fin_Share_Aging_Summary'),
    #End
    # < ------------- Haripriya -------- > Reports  Invoice Details< ------------------------------- >
    path('Fin_Invoice_Report',views.Fin_Invoice_Report, name='Fin_Invoice_Report'),
    path('Fin_InvoiceReportCustomized',views.Fin_InvoiceReportCustomized, name='Fin_InvoiceReportCustomized'),
    path('Fin_share_invoiceDetailsReportToEmail',views.Fin_share_invoiceDetailsReportToEmail, name='Fin_share_invoiceDetailsReportToEmail'),
    #End
    # ------------------------------------ journal Report ------------------------------------
    path('Fin_journel_report',views.Fin_journel_report, name='Fin_journel_report'),
    path('Fin_journalDetailsCustomized',views.Fin_journalDetailsCustomized, name='Fin_journalDetailsCustomized'),
    path('Fin_share_journalDetailsReportToEmail',views.Fin_share_journalDetailsReportToEmail, name='Fin_share_journalDetailsReportToEmail'),
    #End
    # < ------------- Arya E.R -------- > Reports - Credit note details < ------------------------------- >
    path('Fin_creditnoteReport',views.Fin_creditnoteReport, name='Fin_creditnoteReport'),
    path('Fin_creditnoteReportCustomized',views.Fin_creditnoteReportCustomized, name='Fin_creditnoteReportCustomized'),
    path('Fin_sharecreditnoteReportToEmail',views.Fin_sharecreditnoteReportToEmail, name='Fin_sharecreditnoteReportToEmail'),
    # End
    # ------------------------------------ rec bill Report ------------------------------------
    path('Fin_recBill_report',views.Fin_recBill_report, name='Fin_recBill_report'),
    path('Fin_recbillCustomized',views.Fin_recbillCustomized, name='Fin_recbillCustomized'),
    path('Fin_shareREC_billDetailsReportToEmail',views.Fin_shareREC_billDetailsReportToEmail, name='Fin_shareREC_billDetailsReportToEmail'),
    #End
    #  sruthi reports- debit note details---------------------------------
    path('Fin_debitnotereport',views.Fin_debitnotereport, name='Fin_debitnotereport'),
    path('Fin_Debitnotereport_Customized',views.Fin_Debitnotereport_Customized, name='Fin_Debitnotereport_Customized'),
    path('Fin_sharedebitdetailsReportToEmail',views.Fin_sharedebitdetailsReportToEmail, name='Fin_sharedebitdetailsReportToEmail'),
    # end-------------------
    # ashikhvu----------------------------------------bill details report---------------------------------------------
    path('Fin_report_bill_details',views.Fin_report_bill_details, name='Fin_report_bill_details'),
    path('Fin_billCustomized',views.Fin_billCustomized, name='Fin_billCustomized'),
    path('Fin_share_billDetailsReportToEmail',views.Fin_share_billDetailsReportToEmail, name='Fin_share_billDetailsReportToEmail'),
    #End
    # ------------------------------------ vender balance Report ------------------------------------
    path('Fin_venderbalance',views.Fin_venderbalance, name='Fin_venderbalance'),
    path('Fin_vendorbalence_report_customized',views.Fin_vendorbalence_report_customized, name='Fin_vendorbalence_report_customized'),
    path('Fin_share_vendor_BalenceReportToEmail',views.Fin_share_vendor_BalenceReportToEmail, name='Fin_share_vendor_BalenceReportToEmail'),
    #End
    # ------------------------------------ alltransactions Report ------------------------------------
    path('alltransactions',views.alltransactions, name='alltransactions'),
    path('Fin_AlltransactionsCustomized',views.Fin_AlltransactionsCustomized, name='Fin_AlltransactionsCustomized'),
    path('Fin_alltransactionReportToEmail',views.Fin_alltransactionReportToEmail, name='Fin_alltransactionReportToEmail'),
    #End
    #---Updates ----shemeem--------------------------------------------------------
    path('Fin_convert_purchase_order_to_rec_bill/<int:id>',views.Fin_convertPurchaseOrderToRecBill, name='Fin_convertPurchaseOrderToRecBill'),
    path('Fin_purchase_order_convert_rec_bill/<int:id>',views.Fin_purchaseOrderConvertRecBill, name='Fin_purchaseOrderConvertRecBill'),
    path('Fin_TermUpdate_Modules_Action',views.Fin_TermUpdate_Modules_Action,name='Fin_TermUpdate_Modules_Action'),
    path('ATerm_extension_requests', views.Fin_adminTermExtensionRequests, name='Fin_adminTermExtensionRequests'),
    path('Fin_delivery_Challan_Transaction_History/<int:id>',views.Fin_deliveryChallanTransactionHistory, name='Fin_deliveryChallanTransactionHistory'),
    path('Fin_debit_Note_Transaction_History/<int:id>',views.Fin_debitNoteTransactionHistory, name='Fin_debitNoteTransactionHistory'),
    path('Fin_LoanAccountTransactionHistory/<int:id>', views.Fin_LoanAccountTransactionHistory, name='Fin_LoanAccountTransactionHistory'),
    path('Fin_employee_Loan_History/<int:id>',views.Fin_employeeLoanHistory, name='Fin_employeeLoanHistory'),
    path('Fin_employee_Loan_TransHistory/<int:id>',views.Fin_employeeLoanTransHistory, name='Fin_employeeLoanTransHistory'),
    path('Fin_get_bill_numbers',views.Fin_getBillNumbers, name='Fin_getBillNumbers'),
    path('Fin_get_bill_numbers_edit',views.Fin_getBillNumbersEdit, name='Fin_getBillNumbersEdit'),
    path('Fin_get_bill_details',views.Fin_getBillDet, name='Fin_getBillDet'),
    path('Fin_get_bill_paid_amount',views.Fin_getBillPaidAmount, name='Fin_getBillPaidAmount'),
    #End
    # ------------------------------------ gstr1 Report ------------------------------------
    path('gstr1',views.gstr1, name='gstr1'),
    path('Fin_gstr1Customized',views.Fin_gstr1Customized, name='Fin_gstr1Customized'),
    path('Fin_shareGSTR1ReportToEmail',views.Fin_shareGSTR1ReportToEmail, name='Fin_shareGSTR1ReportToEmail'),
    #End
    # ------------------------------------ gstr2 Report ------------------------------------
    path('gstr2',views.gstr2, name='gstr2'),
    path('Fin_gstr2Customized',views.Fin_gstr2Customized, name='Fin_gstr2Customized'),
    path('Fin_shareGSTR2ReportToEmail',views.Fin_shareGSTR2ReportToEmail, name='Fin_shareGSTR2ReportToEmail'),
    #End
    # < ------------- Shemeem -------- > Reports - Cash Flow < ------------------------------- >
    path('Fin_report_cash_flow',views.Fin_cashFlowReport, name='Fin_cashFlowReport'),
    path('Fin_cash_flow_report_customized',views.Fin_cashFlowReportCustomized, name='Fin_cashFlowReportCustomized'),
    path('Fin_share_cash_flow_report_to_email',views.Fin_shareCashFlowReportToEmail, name='Fin_shareCashFlowReportToEmail'),
    # End
    # < ------------- Shemeem -------- > Reports - Party Statements < ------------------------------- >
    path('Fin_report_party_statement',views.Fin_partyStatementReport, name='Fin_partyStatementReport'),
    path('Fin_party_statement_report_customized',views.Fin_partyStatementReportCustomized, name='Fin_partyStatementReportCustomized'),
    path('Fin_share_party_statement_report_to_email',views.Fin_sharePartyStatementReportToEmail, name='Fin_sharePartyStatementReportToEmail'),
    # End
    # ------------------------------------ sale_summary_byHSN Report ------------------------------------
    path('sale_summary_byHSN',views.sale_summary_byHSN, name='sale_summary_byHSN'),
    path('Fin_saleshsnCustomized',views.Fin_saleshsnCustomized, name='Fin_saleshsnCustomized'),
    path('Fin_sharesalesHSNDetailsReportToEmail',views.Fin_sharesalesHSNDetailsReportToEmail, name='Fin_sharesalesHSNDetailsReportToEmail'),
    #End
    # < ------------- Shemeem -------- > Reports - All Parties < ------------------------------- >
    path('Fin_report_all_parties',views.Fin_allPartiesReport, name='Fin_allPartiesReport'),
    path('Fin_all_parties_report_customized',views.Fin_allPartiesReportCustomized, name='Fin_allPartiesReportCustomized'),
    path('Fin_share_all_parties_report_to_email',views.Fin_shareAllPartiesReportToEmail, name='Fin_shareAllPartiesReportToEmail'),
    #End
    # < ------------- Shemeem -------- > Reports - Stock Details < ------------------------------- >
    path('Fin_report_stock_details',views.Fin_stockDetailsReport, name='Fin_stockDetailsReport'),
    path('Fin_share_stock_details_report_to_email',views.Fin_shareStockDetailsReportToEmail, name='Fin_shareStockDetailsReportToEmail'),
    # End
    # ------------------------------------ low stock Report ------------------------------------
    path('Fin_lowstockDetailsReport',views.Fin_lowstockDetailsReport, name='Fin_lowstockDetailsReport'),
    path('Fin_sharelowStockDetailsReportToEmail',views.Fin_sharelowStockDetailsReportToEmail, name='Fin_sharelowStockDetailsReportToEmail'),
    #End
    # ------------------------------------ discount Report ------------------------------------
    path('Fin_sales_item_DiscountReport',views.Fin_sales_item_DiscountReport, name='Fin_sales_item_DiscountReport'),
    path('Fin_sharesales_item_DiscountReportToEmail',views.Fin_sharesales_item_DiscountReportToEmail, name='Fin_sharesales_item_DiscountReportToEmail'),
    #End
    # ------------------------------------ discount Report ------------------------------------
    path('Fin_sales_item_DiscountReportcutomized',views.Fin_sales_item_DiscountReportcutomized, name='Fin_sales_item_DiscountReportcutomized'),
    #End
    # ------------------------------------ Aging Details ------------------------------------
    path('Fin_Aging_Details',views.Fin_aging_details, name='Fin_aging_details'),
    path('Fin_Customize_Aging_Details',views.Fin_customize_aging_details, name='Fin_customize_aging_details'),
    path('Fin_share_aging_details',views.Fin_share_aging_details, name='Fin_share_aging_details'),
    #End
    # < ------------- Shemeem -------- > Reports - Item Report By Party < ------------------------------- >
    path('Fin_report_item_report_by_party',views.Fin_itemReportByParty, name='Fin_itemReportByParty'),
    path('Fin_item_report_by_party_customized',views.Fin_itemReportByPartyCustomized, name='Fin_itemReportByPartyCustomized'),
    path('Fin_share_item_report_by_party_to_email',views.Fin_shareItemReportByPartyToEmail, name='Fin_shareItemReportByPartyToEmail'),
    #End
    # < ------------- Shemeem -------- > Reports - Party Report By Item < ------------------------------- >
    path('Fin_report_party_report_by_item',views.Fin_partyReportByItem, name='Fin_partyReportByItem'),
    path('Fin_party_report_by_item_customized',views.Fin_partyReportByItemCustomized, name='Fin_partyReportByItemCustomized'),
    path('Fin_share_party_report_by_item_to_email',views.Fin_sharePartyReportByItemToEmail, name='Fin_sharePartyReportByItemToEmail'),
    # End
    # ------------------------------------ Payment Received Report ------------------------------------
    path('Fin_PaymentReceived_report',views.Fin_PaymentReceived_report, name='Fin_PaymentReceived_report'),
    path('Fin_payments_receivedCustomized',views.Fin_payments_receivedCustomized, name='Fin_payments_receivedCustomized'),
    path('Fin_sharePaymentsReceivedReportToEmail',views.Fin_sharePaymentsReceivedReportToEmail, name='Fin_sharePaymentsReceivedReportToEmail'),
    #End
    # ------------------------------------ Payment made Report ------------------------------------
    path('Fin_Paymentmade_report',views.Fin_Paymentmade_report, name='Fin_Paymentmade_report'),
    path('Fin_payments_madeCustomized',views.Fin_payments_madeCustomized, name='Fin_payments_madeCustomized'),
    path('Fin_sharePaymentsmadeReportToEmail',views.Fin_sharePaymentsmadeReportToEmail, name='Fin_sharePaymentsmadeReportToEmail'),
    #End
    # < ------------- Shemeem -------- > Reports - Expense Reports < ------------------------------- >
    path('Fin_expense_report',views.Fin_expenseReport, name='Fin_expenseReport'),
    path('Fin_expense_report_customized',views.Fin_expenseReportCustomized, name='Fin_expenseReportCustomized'),
    path('Fin_share_expense_report_to_email',views.Fin_shareExpenseReportToEmail, name='Fin_shareExpenseReportToEmail'),
    # End
    # < ------------- Shemeem -------- > Reports - EWay Bills Reports < ------------------------------- >
    path('Fin_eway_bill_report',views.Fin_ewayBillReport, name='Fin_ewayBillReport'),
    path('Fin_eway_bill_report_customized',views.Fin_ewayBillReportCustomized, name='Fin_ewayBillReportCustomized'),
    path('Fin_share_eway_bill_report_to_email',views.Fin_shareEwayBillReportToEmail, name='Fin_shareEwayBillReportToEmail'),
    # End
    #---------------------------------------Loan Account & Bank Report--------------------
    path('Fin_loanAccountReport',views.Fin_loanAccountReport, name='Fin_loanAccountReport'),
    path('Fin_shareloanaccountReportToEmail',views.Fin_shareloanaccountReportToEmail, name='Fin_shareloanaccountReportToEmail'),
    path('Fin_BankReport',views.Fin_BankReport, name='Fin_BankReport'),
    path('Fin_shareBankReportToEmail',views.Fin_shareBankReportToEmail, name='Fin_shareBankReportToEmail'),
    #End
    # harikrishnan ------- discount report -------------------------
    path('Fin_discount_report',views.Fin_discount_report,name="Fin_discount_report"),
    path('discount_report_date_filter',views.discount_report_date_filter,name="discount_report_date_filter"),
    path('sendEmail_discount_report',views.sendEmail_discount_report,name="sendEmail_discount_report"),
    #End
    path('stocksummary', views.stocksummary, name='stocksummary'),
    #---------------------------------------salesby purchase& inventory--------------------   
    path('Fin_salespurchasebypartyReport',views.Fin_salespurchasebypartyReport, name='Fin_salespurchasebypartyReport'),
    path('Fin_sharePurchaseBySalesReportToEmail',views.Fin_sharePurchaseBySalesReportToEmail, name='Fin_sharePurchaseBySalesReportToEmail'),
    path('Fin_InventoryItemReport',views.Fin_InventoryItemReport, name='Fin_InventoryItemReport'),
    path('Fin_shareInventoryReportToEmail',views.Fin_shareInventoryReportToEmail, name='Fin_shareInventoryReportToEmail'),
    #End
    # ------------------------------------ trial balance Report ------------------------------------
    path('Fin_trial_balance',views.Fin_trial_balance, name='Fin_trial_balance'),
    path('Fin_trial_balancecustomized',views.Fin_trial_balancecustomized, name='Fin_trial_balancecustomized'),
    path('Fin_shareFin_trial_balanceToEmail',views.Fin_shareFin_trial_balanceToEmail, name='Fin_shareFin_trial_balanceToEmail'),
    #End
    # < ------------- Harikrishnan -------- > Reports - Fin_employee_loan_details < ------------------------------- >
    path('Fin_employee_loan_statement_report',views.Fin_employee_loan_statement_report,name="Fin_employee_loan_statement_report"),
    path('employee_loan_statement_report_date_filter',views.employee_loan_statement_report_date_filter,name="employee_loan_statement_report_date_filter"),
    path('sendEmail_employee_loan_statement_report',views.sendEmail_employee_loan_statement_report,name="sendEmail_employee_loan_statement_report"),
    #End
    # ashikh------------------------------------------report outstanding payables-----------------------------------------
    path('Fin_report_account_outstanding_payables',views.Fin_report_account_outstanding_payables, name='Fin_report_account_outstanding_payables'),
    path('Fin_report_account_outstanding_payables_tomail',views.Fin_report_account_outstanding_payables_tomail, name='Fin_report_account_outstanding_payables_tomail'),
    #End
    # ashikh------------------------------------------report outstanding receivable-----------------------------------------
    path('Fin_report_account_outstanding_receivable',views.Fin_report_account_outstanding_receivable, name='Fin_report_account_outstanding_receivable'),
    path('Fin_report_account_outstanding_receivable_tomail',views.Fin_report_account_outstanding_receivable_tomail, name='Fin_report_account_outstanding_receivable_tomail'),
    #End
    # sales and purchase order item details - harikrishnan ----------
    path('Fin_sales_order_item_details',views.Fin_sales_order_item_details,name="Fin_sales_order_item_details"),
    path('sales_order_item_details_date_filter',views.sales_order_item_details_date_filter,name="sales_order_item_details_date_filter"),
    path('sendEmail_sales_order_item_details',views.sendEmail_sales_order_item_details,name="sendEmail_sales_order_item_details"),
    path('Fin_purchase_order_item_details',views.Fin_purchase_order_item_details,name="Fin_purchase_order_item_details"),
    path('purchase_order_item_details_date_filter',views.purchase_order_item_details_date_filter,name="purchase_order_item_details_date_filter"),
    path('sendEmail_purchase_order_item_details',views.sendEmail_purchase_order_item_details,name="sendEmail_purchase_order_item_details"),
    #End
    #---------------------------------------payment recived summary& payment made summary--------------------
    path('Fin_paymentRecivedReport',views.Fin_paymentRecivedReport, name='Fin_paymentRecivedReport'),
    path('Fin_sharePaymentrecivedReportToEmail',views.Fin_sharePaymentrecivedReportToEmail, name='Fin_sharePaymentrecivedReportToEmail'),
    path('Fin_paymentMadeSummaryReport',views.Fin_paymentMadeSummaryReport, name='Fin_paymentMadeSummaryReport'),
    path('Fin_sharePaymentmadeReportToEmail',views.Fin_sharePaymentmadeReportToEmail, name='Fin_sharePaymentmadeReportToEmail'),
    #End
    path('stocksummary2', views.stocksummary2, name='stocksummary2'),
    path('stocksummary1', views.stocksummary1, name='stocksummary1'),
    path('Fin_shareStockSummaryToEmail', views.Fin_shareStockSummaryToEmail, name='Fin_shareStockSummaryToEmail'),
    #---------------------------------------profit & loss A/C--------------------
    path('fin_profit_loss', views.fin_profit_loss, name='fin_profitloss'),
    path('fin_profitloss_mail', views.fin_profitloss_mail, name='fin_profitlossmail'),  
    #End
    #---------------------------------------horizontal profit & loss A/C--------------------  
    path('horizontal_profit_loss', views.horizontal_profit_loss, name='horizontal_profitloss'),
    path('horizontal_profitloss_mail', views.horizontal_profitloss_mail, name='horizontal_profitlossmail'), 
    # End

    #---------------------------------------Balance sheet-------------------- 
    path('balance_sheet', views.balance_sheet, name='balancesheet'),
    path('balance_sheet_mail', views.balance_sheet_mail, name='balance_sheet_mail'),
    # End

    #---------------------------------------Vertical Balance sheet-------------------- 
    path('vertical_balance_sheet', views.vertical_balance_sheet, name='vertical_balance_sheet'),
    path('vertical_balance_sheet_mail', views.vertical_balance_sheet_mail, name='vertical_balance_sheetmail'),
    # End

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)