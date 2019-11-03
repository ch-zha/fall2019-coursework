-- #1
select distinct vendor_name from vendors
	where vendor_id in (select vendor_id from invoices)
	order by vendor_name;

-- #2
select invoice_number, invoice_total from invoices
	where payment_total > (select avg(payment_total) from invoices where payment_total > 0)
    order by invoice_total desc;

-- #3
select account_number, account_description from general_ledger_accounts g
	where not exists(select * from invoice_line_items i where i.account_number = g.account_number)
    order by account_number;

-- #4
select vendor_name, invoice_id, invoice_sequence, line_item_amount
	from vendors v
    join invoices i using (vendor_id)
	join invoice_line_items l using (invoice_id)
    where invoice_id in (select distinct invoice_id from invoice_line_items where invoice_sequence > 1)
    order by vendor_name, invoice_id, invoice_sequence;

-- #5
select vendor_id, max(invoice_total) as largest_unpaid_invoice
	from invoices
    where payment_date is null
    group by vendor_id;

select sum(l.largest_unpaid_invoice) as sum
	from (
		select vendor_id, max(invoice_total) as largest_unpaid_invoice
		from invoices
		where payment_date is null
		group by vendor_id
        ) l;

-- #6
select vendor_name, vendor_city, vendor_state from vendors
	where vendor_id not in (
		select v1.vendor_id from vendors v1 join vendors v2
		where v1.vendor_city = v2.vendor_city
			and v1.vendor_state = v2.vendor_state
			and v1.vendor_id != v2.vendor_id
        )
	order by vendor_state, vendor_city;

-- #7
select vendor_name, invoice_number, invoice_date, invoice_total
	from vendors join invoices i1 using (vendor_id)
    where invoice_date = (select min(invoice_date) from invoices i2 where i1.vendor_id = i2.vendor_id)
    order by vendor_name;
