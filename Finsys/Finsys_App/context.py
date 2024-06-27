from .models import *

def minStock(request):
    if 's_id' in request.session:
        s_id = request.session['s_id']
        data = Fin_Login_Details.objects.get(id = s_id)
        if data.User_Type != 'Distributor':
            if data.User_Type == "Company":
                com = Fin_Company_Details.objects.get(Login_Id = s_id)
            elif data.User_Type == 'Staff':
                com = Fin_Staff_Details.objects.get(Login_Id = s_id).company_id
            
            itemsAvailable = Fin_Items.objects.filter(Company = com)

            if Fin_CNotification.objects.filter(Company_id=com, Item__isnull=False).exists():
                alertItems = Fin_CNotification.objects.filter(Company_id=com, Item__isnull=False)
                for item in alertItems:
                    stockItem = Fin_Items.objects.get(id = item.Item.id)
                    if stockItem.current_stock > stockItem.min_stock:
                        item.status = 'Old'
                        item.save()
                    else:
                        item.status = 'New'
                        item.save()
                
                for itm in itemsAvailable:
                    if not Fin_CNotification.objects.filter(Item = itm).exists():
                        if itm.min_stock > 0 and itm.current_stock < itm.min_stock:
                            Fin_CNotification.objects.create(Company_id = com, Login_Id = data, Item = itm, Title = 'Stock Alert.!!', Discription = f'{itm.name} is below the minimum stock threshold..')

            else:
                for itm in itemsAvailable:
                    if itm.min_stock > 0 and itm.current_stock < itm.min_stock:
                        Fin_CNotification.objects.create(Company_id = com, Login_Id = data, Item = itm, Title = 'Stock Alert.!!', Discription = f'{itm.name} is below the minimum stock threshold..')
            
            stockLow = Fin_CNotification.objects.filter(Company_id = com, Item__isnull=False, status = 'New')
            nCount = Fin_CNotification.objects.filter(Company_id = com, status = 'New')
            if stockLow:
                context = {
                    'stockAlert': True,
                    'stockLow': stockLow,
                    'n': len(nCount)
                }    
                return context
            else:
                return {'alert': False,'n': len(nCount)}
        else:
            return {'alert': False}    
    else:
        return {'alert': False}
        
        
def creditLimitAlert(request):
    if 's_id' in request.session:
        s_id = request.session['s_id']
        data = Fin_Login_Details.objects.get(id = s_id)
        if data.User_Type == "Company":
            com = Fin_Company_Details.objects.get(Login_Id = s_id)
        else:
            com = Fin_Staff_Details.objects.get(Login_Id = s_id).company_id
        
        customers = Fin_Customers.objects.filter(Company = com)

        if Fin_CNotification.objects.filter(Company_id=com, Customers__isnull=False).exists():
            alertItems = Fin_CNotification.objects.filter(Company_id=com, Customers__isnull=False)
            for c in alertItems:
                cust = Fin_Customers.objects.get(id = c.Customers.id)
                if cust.credit_limit > cust.current_balance:
                    c.status = 'Old'
                    c.save()
                else:
                    c.status = 'New'
                    c.save()
            
            for itm in customers:
                if not Fin_CNotification.objects.filter(Customers = itm).exists():
                    if itm.current_balance > itm.credit_limit:
                        Fin_CNotification.objects.create(Company_id = com, Login_Id = data, Customers = itm, Title = 'Credit Limit Alert.!!', Discription = f'{itm.first_name} {itm.last_name} has been exceeded the credit limit..')

        else:
            for itm in customers:
                if itm.current_balance > itm.credit_limit:
                    Fin_CNotification.objects.create(Company_id = com, Login_Id = data, Customers = itm, Title = 'Credit Limit Alert.!!', Discription = f'{itm.first_name} {itm.last_name} has been exceeded the credit limit..')
        
        creditLimit = Fin_CNotification.objects.filter(Company_id = com, Customers__isnull=False, status = 'New')
        nCount = Fin_CNotification.objects.filter(Company_id = com, status = 'New')
        if creditLimit:
            context = {
                'creditLimitAlert': True,
                'creditLimit': creditLimit,
                'n': len(nCount)
            }    
            return context
        else:
            return {'alert': False,'n': len(nCount)}
    else:
        return {'alert': False}
        
        
def customerCreditLimitAlert(request):
    if 's_id' in request.session:
        s_id = request.session['s_id']
        data = Fin_Login_Details.objects.get(id = s_id)
        if data.User_Type != 'Distributor':
            if data.User_Type == "Company":
                com = Fin_Company_Details.objects.get(Login_Id = s_id)
            elif data.User_Type == 'Staff':
                com = Fin_Staff_Details.objects.get(Login_Id = s_id).company_id
            
            customers = Fin_Customers.objects.filter(Company = com)

            if Fin_CNotification.objects.filter(Company_id=com, Customers__isnull=False).exists():
                alertItems = Fin_CNotification.objects.filter(Company_id=com, Customers__isnull=False)
                for c in alertItems:
                    cust = Fin_Customers.objects.get(id = c.Customers.id)
                    if cust.credit_limit > 0 and cust.credit_limit > cust.current_balance:
                        c.status = 'Old'
                        c.save()
                    else:
                        c.status = 'New'
                        c.save()
                
                for itm in customers:
                    if not Fin_CNotification.objects.filter(Customers = itm).exists():
                        if itm.credit_limit > 0 and itm.current_balance > itm.credit_limit:
                            Fin_CNotification.objects.create(Company_id = com, Login_Id = data, Customers = itm, Title = 'Customer Credit Limit Alert.!!', Discription = f'{itm.first_name} {itm.last_name} has been exceeded the credit limit..')

            else:
                for itm in customers:
                    if itm.credit_limit > 0 and itm.current_balance > itm.credit_limit:
                        Fin_CNotification.objects.create(Company_id = com, Login_Id = data, Customers = itm, Title = 'Customer Credit Limit Alert.!!', Discription = f'{itm.first_name} {itm.last_name} has been exceeded the credit limit..')
            
            custCreditLimit = Fin_CNotification.objects.filter(Company_id = com, Customers__isnull=False, status = 'New')
            nCount = Fin_CNotification.objects.filter(Company_id = com, status = 'New')
            if custCreditLimit:
                context = {
                    'cCreditLimitAlert': True,
                    'cCreditLimit': custCreditLimit,
                    'n': len(nCount)
                }    
                return context
            else:
                return {'alert': False,'n': len(nCount)}
        else:
            return {'alert': False}
    else:
        return {'alert': False}
        
        
def vendorCreditLimitAlert(request):
    if 's_id' in request.session:
        s_id = request.session['s_id']
        data = Fin_Login_Details.objects.get(id = s_id)
        if data.User_Type != 'Distributor':
            if data.User_Type == "Company":
                com = Fin_Company_Details.objects.get(Login_Id = s_id)
            elif data.User_Type == 'Staff':
                com = Fin_Staff_Details.objects.get(Login_Id = s_id).company_id
            
            vendors = Fin_Vendors.objects.filter(Company = com)

            if Fin_CNotification.objects.filter(Company_id=com, Vendors__isnull=False).exists():
                alertItems = Fin_CNotification.objects.filter(Company_id=com, Vendors__isnull=False)
                for c in alertItems:
                    vnd = Fin_Vendors.objects.get(id = c.Vendors.id)
                    if vnd.credit_limit != 0 and vnd.credit_limit > vnd.current_balance:
                        c.status = 'New'
                        c.save()
                    else:
                        c.status = 'Old'
                        c.save()
                
                for itm in vendors:
                    if not Fin_CNotification.objects.filter(Vendors = itm).exists():
                        if itm.credit_limit != 0 and itm.credit_limit > itm.current_balance:
                            Fin_CNotification.objects.create(Company_id = com, Login_Id = data, Vendors = itm, Title = 'Vendor Credit Limit Alert.!!', Discription = f'{itm.first_name} {itm.last_name} has been exceeded the credit limit..')

            else:
                for itm in vendors:
                    if itm.credit_limit != 0 and itm.credit_limit > itm.current_balance:
                        Fin_CNotification.objects.create(Company_id = com, Login_Id = data, Vendors = itm, Title = 'Vendor Credit Limit Alert.!!', Discription = f'{itm.first_name} {itm.last_name} has been exceeded the credit limit..')
            
            vendorCreditLimit = Fin_CNotification.objects.filter(Company_id = com, Vendors__isnull=False, status = 'New')
            nCount = Fin_CNotification.objects.filter(Company_id = com, status = 'New')
            if vendorCreditLimit:
                context = {
                    'vCreditLimitAlert': True,
                    'vCreditLimit': vendorCreditLimit,
                    'n': len(nCount)
                }    
                return context
            else:
                return {'alert': False,'n': len(nCount)}
        else:
            return {'alert': False}
    else:
        return {'alert': False}