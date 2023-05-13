{"filter":false,"title":"delete_item_from_dynamo_db_table.py","tooltip":"/dynamo_db_functions/delete_item_from_dynamo_db_table.py","undoManager":{"mark":27,"position":27,"stack":[[{"start":{"row":13,"column":9},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":14,"column":0},"end":{"row":14,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":14,"column":8},"end":{"row":15,"column":0},"action":"insert","lines":["       'request_id': 'request_id',",""],"id":4}],[{"start":{"row":14,"column":42},"end":{"row":15,"column":0},"action":"remove","lines":["",""],"id":5}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":12},"action":"remove","lines":["    "],"id":6},{"start":{"row":14,"column":4},"end":{"row":14,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"remove","lines":["       'request_id': 'request_id',",""],"id":7}],[{"start":{"row":14,"column":7},"end":{"row":15,"column":26},"action":"remove","lines":[" 'username': 'janedoe',","        'last_name': 'Doe'"],"id":19},{"start":{"row":14,"column":7},"end":{"row":19,"column":40},"action":"insert","lines":[" 'request_id': 'request_id',","        'username': 'janedoe',","        'first_name': 'Jane',","        'last_name': 'Doe',","        'age': 25,","        'account_type': 'standard_user',"]}],[{"start":{"row":15,"column":4},"end":{"row":16,"column":29},"action":"remove","lines":["    'username': 'janedoe',","        'first_name': 'Jane',"],"id":20}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["\\"],"id":21}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"remove","lines":["\\"],"id":22},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":14,"column":35},"end":{"row":15,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":17,"column":40},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":18,"column":0},"end":{"row":18,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":18,"column":8},"end":{"row":19,"column":29},"action":"insert","lines":["    'username': 'janedoe',","        'first_name': 'Jane',"],"id":24}],[{"start":{"row":15,"column":27},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":25},{"start":{"row":16,"column":0},"end":{"row":16,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":16,"column":8},"end":{"row":17,"column":0},"action":"insert","lines":["        'account_type': 'standard_user',",""],"id":26}],[{"start":{"row":16,"column":48},"end":{"row":17,"column":0},"action":"remove","lines":["",""],"id":27}],[{"start":{"row":16,"column":12},"end":{"row":16,"column":16},"action":"remove","lines":["    "],"id":28},{"start":{"row":16,"column":8},"end":{"row":16,"column":12},"action":"remove","lines":["    "]}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"remove","lines":["        'account_type': 'standard_user',",""],"id":29}],[{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"remove","lines":["        'first_name': 'Jane',",""],"id":30}],[{"start":{"row":18,"column":8},"end":{"row":18,"column":12},"action":"remove","lines":["    "],"id":31}],[{"start":{"row":17,"column":18},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":32},{"start":{"row":18,"column":0},"end":{"row":18,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":18,"column":8},"end":{"row":19,"column":0},"action":"insert","lines":["        'first_name': 'Jane',",""],"id":33}],[{"start":{"row":18,"column":37},"end":{"row":19,"column":0},"action":"remove","lines":["",""],"id":34}],[{"start":{"row":18,"column":12},"end":{"row":18,"column":16},"action":"remove","lines":["    "],"id":35},{"start":{"row":18,"column":8},"end":{"row":18,"column":12},"action":"remove","lines":["    "]}],[{"start":{"row":14,"column":7},"end":{"row":19,"column":30},"action":"remove","lines":[" 'request_id': 'request_id',","        'last_name': 'Doe',","        'account_type': 'standard_user',","        'age': 25,","        'first_name': 'Jane',","        'username': 'janedoe',"],"id":36},{"start":{"row":14,"column":7},"end":{"row":19,"column":40},"action":"insert","lines":[" 'request_id': 'Name',","        'username': 'janedoe',","        'first_name': 'Jane',","        'last_name': 'Doe',","        'age': 25,","        'account_type': 'standard_user',"]}],[{"start":{"row":19,"column":39},"end":{"row":19,"column":40},"action":"remove","lines":[","],"id":37}],[{"start":{"row":14,"column":7},"end":{"row":19,"column":39},"action":"remove","lines":[" 'request_id': 'Name',","        'username': 'janedoe',","        'first_name': 'Jane',","        'last_name': 'Doe',","        'age': 25,","        'account_type': 'standard_user'"],"id":38},{"start":{"row":14,"column":7},"end":{"row":19,"column":39},"action":"insert","lines":["'request_id': 'Name',","        'username': 'janedoe',","        'first_name': 'Jane',","        'last_name': 'Doe',","        'age': 25,","        'account_type': 'standard_user'"]}],[{"start":{"row":15,"column":0},"end":{"row":16,"column":29},"action":"remove","lines":["        'username': 'janedoe',","        'first_name': 'Jane',"],"id":42},{"start":{"row":14,"column":28},"end":{"row":15,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":39},"action":"remove","lines":["        'age': 25,","        'account_type': 'standard_user'"],"id":43},{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"insert","lines":["="]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"remove","lines":["="],"id":44},{"start":{"row":15,"column":27},"end":{"row":16,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":134.5,"scrollleft":0,"selection":{"start":{"row":17,"column":1},"end":{"row":17,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":7,"state":"start","mode":"ace/mode/python"}},"timestamp":1683864958132,"hash":"f11c7c1ffefd7e70ed5ffc15079d89b0e0e7ba1f"}}