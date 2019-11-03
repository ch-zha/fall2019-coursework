-- #1
insert terms
	values (6, 'Net due 120 days', 120);

-- #2
update terms
	set terms_description = 'Net due 125 days',
		terms_due_days = 125
	where terms_id = 6;

-- #3
delete from terms
	where terms_id = 6;
    
-- #4
insert invoices
	values (default, 32, 'AX-014-027', '2018-08-01', 434.58, 0, 0, 2, '2018-08-31', null);

-- #5
insert invoice_line_items
	select invoice_id, 1, 160, 180.23, 'Hard drive'
        from invoices where invoice_number = 'AX-014-027'
	union
		select invoice_id, 2, 527, 254.35, 'Exchange Server update'
        from invoices where invoice_number = 'AX-014-027';

-- #6
update invoices
	set credit_total = invoice_total * .1,
		payment_total = invoice_total - credit_total
	where invoice_number = 'AX-014-027';

-- #7
update vendors
	set default_account_number = 403
    where vendor_id = 44;

-- #8
update invoices
	set terms_id = 2
    where vendor_id in 
		(select vendor_id from vendors where default_terms_id = 2);

-- #9
delete from invoice_line_items
	where invoice_id in
		(select invoice_id from invoices where invoice_number = 'AX-014-027');
delete from invoices
	where invoice_number = 'AX-014-027';