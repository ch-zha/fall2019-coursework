-- #1
select vendor_id,
	sum(invoice_total) as invoice_total_sum
	from invoices
    group by vendor_id;

-- #2
select vendor_name, sum(payment_total) as payment_total_sum
	from vendors
join invoices i using (vendor_id)
group by vendor_id
order by payment_total_sum desc;

-- #3
select vendor_name,
	count(all invoice_id) as invoice_count,
    sum(invoice_total) as invoice_total_sum
from vendors join invoices i using (vendor_id)
group by vendor_id
order by invoice_count desc;

-- #4
select account_description,
	count(*) as line_items_count,
    sum(line_item_amount) as line_items_amount_sum
from general_ledger_accounts g join invoice_line_items using (account_number)
group by g.account_description
having line_items_count > 1
order by line_items_amount_sum desc;

-- #5
select account_description,
	count(*) as line_items_count,
    sum(line_item_amount) as line_items_amount_sum
from general_ledger_accounts g
	join invoice_line_items using (account_number)
    join invoices using (invoice_id)
    where invoice_date > '2018-04-01' and invoice_date < '2018-06-30'
group by g.account_description
having line_items_count > 1
order by line_items_amount_sum desc;

-- #6
select account_number, sum(line_item_amount) as line_item_amount_sum
	from invoice_line_items
group by account_number with rollup;

-- #7
select vendor_name, count(distinct account_number) as number_of_accounts
	from vendors
		join invoices i using (vendor_id)
		join invoice_line_items l using (invoice_id)
		join general_ledger_accounts g using (account_number)
	group by vendor_id
    having number_of_accounts > 1;

-- #8
select if(grouping(terms_id) = 1, 'Terms Summary', terms_id) as terms_id,
	if(grouping(vendor_id) = 1, 'Vendor Summary', vendor_id) as vendor_id,
	max(payment_date) as last_payment_date,
    sum(invoice_total - payment_total - credit_total) as balance_due_sum
	from invoices
    group by terms_id, vendor_id with rollup;
    
-- #9
