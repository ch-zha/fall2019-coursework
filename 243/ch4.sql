-- #1
select *
	from vendors
	natural join invoices;

-- #2
select vendor_name, invoice_number, invoice_date,
		invoice_total - payment_total - credit_total as balance_due
	from vendors v
    join invoices i using (vendor_id)
    where invoice_total - payment_total - credit_total > 0
    order by vendor_name asc;
    
-- #3
select vendor_name,
		default_account_number as default_account,
        account_description as description
	from vendors v
    join general_ledger_accounts g
		on g.account_number = v.default_account_number
	order by account_description, vendor_name;
    
-- #4
select vendor_name, invoice_date, invoice_number,
		invoice_sequence as li_sequence,
        line_item_amount as li_amount
	from vendors v
    join invoices i using (vendor_id)
    join invoice_line_items l using (invoice_id)
    order by vendor_name, invoice_date, invoice_number, invoice_sequence;

-- #5
select v1.vendor_id, v1.vendor_name, concat(v1.vendor_contact_first_name, ' ', v1.vendor_contact_last_name) as contact_name
	from vendors v1 join vendors v2
		on v1.vendor_contact_last_name = v2.vendor_contact_last_name and v1.vendor_id != v2.vendor_id
	order by v1.vendor_contact_last_name;
    
-- #6
select account_number, account_description, invoice_id
	from general_ledger_accounts
    left join invoice_line_items using (account_number)
	where invoice_id is null;

-- #7
select vendor_name, vendor_state
	from vendors
    where vendor_state = "CA"
union
select vendor_name, 'Outside CA' as vendor_state
	from vendors
    where vendor_state != "CA"
order by vendor_name;