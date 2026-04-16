% Pizza menu with price
:- dynamic menu/2.
menu(veg_pizza, 249).
menu(chicken_pizza, 399).
menu(pepperoni_pizza, 459).
menu(burger, 149).
menu(coke, 49).

% Start the ordering process
start_order :-
    writeln('--- MENU ---'),
    forall(menu(Item, Price), (write(Item), write(' - Rs.'), writeln(Price))),
    writeln('\nEnter items (type "done." to finish).'),
    % Start loop with empty list [] and 0 total
    order_loop([], 0).

% Recursive loop to get multiple items
order_loop(OrderList, Total) :-
    write('\nEnter Item Name: '), read(Item),
    (   Item == done
    ->  print_receipt(OrderList, Total)
    ;   menu(Item, Price)
    ->  write('Enter Quantity: '), read(Qty),
        Sub is Price * Qty,
        NewTotal is Total + Sub,
        % Add this item's details to the list and continue
        order_loop([[Item, Qty, Sub] | OrderList], NewTotal)
    ;   writeln('Item not in menu. Try again.'),
        order_loop(OrderList, Total)
    ).

% Print the final summary
print_receipt([], _) :- writeln('\nNo items ordered.').
print_receipt(List, Total) :-
    writeln('\n---------- RECEIPT ----------'),
    writeln('ITEM           | QTY | SUB-TOTAL'),
    writeln('-----------------------------'),
    print_items(List),
    writeln('-----------------------------'),
    format('GRAND TOTAL:      Rs.~w~n', [Total]),
    writeln('-----------------------------').

% Helper to print each item from the list
print_items([]).
print_items([[Name, Qty, Sub]|T]) :-
    format('~w~t~15| | ~w~t~20| | Rs.~w~n', [Name, Qty, Sub]),
    print_items(T).