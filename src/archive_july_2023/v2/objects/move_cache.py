PAWN = {
    'w': {
        'a': [
            [],
            ['a3', 'a4', 'b3'],
            ['a4', 'b4'],
            ['a5', 'b5'],
            ['a6', 'b6'],
            ['a7', 'b7'],
            ['a8', 'b8'],
            []
        ], 'b': [
            [],
            ['b3', 'b4', 'a3', 'c3'],
            ['b4', 'a4', 'c4'],
            ['b5', 'a5', 'c5'],
            ['b6', 'a6', 'c6'],
            ['b7', 'a7', 'c7'],
            ['b8', 'a8', 'c8'],
            []
        ], 'c': [
            [],
            ['c3', 'c4', 'b3', 'd3'],
            ['c4', 'b4', 'd4'],
            ['c5', 'b5', 'd5'],
            ['c6', 'b6', 'd6'],
            ['c7', 'b7', 'd7'],
            ['c8', 'b8', 'd8'],
            []
        ], 'd': [
            [],
            ['d3', 'd4', 'c3', 'e3'],
            ['d4', 'c4', 'e4'],
            ['d5', 'c5', 'e5'],
            ['d6', 'c6', 'e6'],
            ['d7', 'c7', 'e7'],
            ['d8', 'c8', 'e8'],
            []
        ], 'e': [
            [],
            ['e3', 'e4', 'd3', 'f3'],
            ['e4', 'd4', 'f4'],
            ['e5', 'd5', 'f5'],
            ['e6', 'd6', 'f6'],
            ['e7', 'd7', 'f7'],
            ['e8', 'd8', 'f8'],
            []
        ], 'f': [
            [],
            ['f3', 'f4', 'e3', 'g3'],
            ['f4', 'e4', 'g4'],
            ['f5', 'e5', 'g5'],
            ['f6', 'e6', 'g6'],
            ['f7', 'e7', 'g7'],
            ['f8', 'e8', 'g8'],
            []
        ], 'g': [
            [],
            ['g3', 'g4', 'f3', 'h3'],
            ['g4', 'f4', 'h4'],
            ['g5', 'f5', 'h5'],
            ['g6', 'f6', 'h6'],
            ['g7', 'f7', 'h7'],
            ['g8', 'f8', 'h8'],
            []
        ], 'h': [
            [],
            ['h3', 'h4', 'g3'],
            ['h4', 'g4'],
            ['h5', 'g5'],
            ['h6', 'g6'],
            ['h7', 'g7'],
            ['h8', 'g8'],
            []
        ]
    },
    'b': {
        'a': [
            []
            ['a5', 'a6', 'b6'],
            ['a5', 'b5'],
            ['a4', 'b4'],
            ['a3', 'b3'],
            ['a2', 'b2'],
            ['a1', 'b1'],
            []
        ], 'b': [
            [],
            ['a6', 'b5', 'b6', 'c6'],
            ['a5', 'b5', 'c5'],
            ['a4', 'b4', 'c4'],
            ['a3', 'b3', 'c3'],
            ['a2', 'b2', 'c2'],
            ['a1', 'b1', 'c1'],
            []
        ], 'c': [
            ['b6', 'c5', 'c6', 'd6'],
            ['b5', 'c5', 'd5'],
            ['b4', 'c4', 'd4'],
            ['b3', 'c3', 'd3'],
            ['b2', 'c2', 'd2'],
            ['b1', 'c1', 'd1'],
            []
        ], 'd': [
            [],
            ['c6', 'd5', 'd6', 'e6'],
            ['c5', 'd5', 'e5'],
            ['c4', 'd4', 'e4'],
            ['c3', 'd3', 'e3'],
            ['c2', 'd2', 'e2'],
            ['c1', 'd1', 'e1'],
            []
        ], 'e': [
            [],
            ['d6', 'e5', 'e6', 'f6'],
            ['d5', 'e5', 'f5'],
            ['d4', 'e4', 'f4'],
            ['d3', 'e3', 'f3'],
            ['d2', 'e2', 'f2'],
            ['d1', 'e1', 'f1'],
            []
        ], 'f': [
            [],
            ['e6', 'f5', 'f6', 'g6'],
            ['e5', 'f5', 'g5'],
            ['e4', 'f4', 'g4'],
            ['e3', 'f3', 'g3'],
            ['e2', 'f2', 'g2'],
            ['e1', 'f1', 'g1'],
            []
        ], 'g': [
            [],
            ['f6', 'g5', 'g6', 'h6'],
            ['f5', 'g5', 'h5'],
            ['f4', 'g4', 'h4'],
            ['f3', 'g3', 'h3'],
            ['f2', 'g2', 'h2'],
            ['f1', 'g1', 'h1'],
            []
        ], 'h': [
            [],
            ['g6', 'h5', 'h6'],
            ['g5', 'h5'],
            ['g4', 'h4'],
            ['g3', 'h3'],
            ['g2', 'h2'],
            ['g1', 'h1'],
            []
        ]
    }
}

KNIGHT = {
    'a': [
        ['b3', 'c2'],
        ['b4', 'c1', 'c3'],
        ['b1', 'b5', 'c2', 'c4'],
        ['b2', 'b6', 'c3', 'c5'],
        ['b3', 'b7', 'c4', 'c6'],
        ['b4', 'b8', 'c5', 'c7'],
        ['b5', 'c6', 'c8'],
        ['b6', 'c7']
    ], 'b': [
        ['a3', 'c3', 'd2'],
        ['a4', 'c4', 'd1', 'd3'],
        ['a1', 'a5', 'c1', 'c5', 'd2', 'd4'],
        ['a2', 'a6', 'c2', 'c6', 'd3', 'd5'],
        ['a3', 'a7', 'c3', 'c7', 'd4', 'd6'],
        ['a4', 'a8', 'c4', 'c8', 'd5', 'd7'],
        ['a5', 'c5', 'd6', 'd8'],
        ['a6', 'c6', 'd7']
    ], 'c': [
        ['a2', 'b3', 'd3', 'e2'],
        ['a1', 'a3', 'b4', 'd4', 'e1', 'e3'],
        ['a2', 'a4', 'b1', 'b5', 'd1', 'd5', 'e2', 'e4'],
        ['a3', 'a5', 'b2', 'b6', 'd2', 'd6', 'e3', 'e5'],
        ['a4', 'a6', 'b3', 'b7', 'd3', 'd7', 'e4', 'e6'],
        ['a5', 'a7', 'b4', 'b8', 'd4', 'd8', 'e5', 'e7'],
        ['a6', 'a8', 'b5', 'd5', 'e6', 'e8'],
        ['a7', 'b6', 'd6', 'e7']
    ], 'd': [
        ['b2', 'c3', 'e3', 'f2'],
        ['b1', 'b3', 'c4', 'e4', 'f1', 'f3'],
        ['b2', 'b4', 'c1', 'c5', 'e1', 'e5', 'f2', 'f4'],
        ['b3', 'b5', 'c2', 'c6', 'e2', 'e6', 'f3', 'f5'],
        ['b4', 'b6', 'c3', 'c7', 'e3', 'e7', 'f4', 'f6'],
        ['b5', 'b7', 'c4', 'c8', 'e4', 'e8', 'f5', 'f7'],
        ['b6', 'b8', 'c5', 'e5', 'f6', 'f8'],
        ['b7', 'c6', 'e6', 'f7']
    ], 'e': [
        ['c2', 'd3', 'f3', 'g2'],
        ['c1', 'c3', 'd4', 'f4', 'g1', 'g3'],
        ['c2', 'c4', 'd1', 'd5', 'f1', 'f5', 'g2', 'g4'],
        ['c3', 'c5', 'd2', 'd6', 'f2', 'f6', 'g3', 'g5'],
        ['c4', 'c6', 'd3', 'd7', 'f3', 'f7', 'g4', 'g6'],
        ['c5', 'c7', 'd4', 'd8', 'f4', 'f8', 'g5', 'g7'],
        ['c6', 'c8', 'd5', 'f5', 'g6', 'g8'],
        ['c7', 'd6', 'f6', 'g7']
    ], 'f': [
        ['d2', 'e3', 'g3', 'h2'],
        ['d1', 'd3', 'e4', 'g4', 'h1', 'h3'],
        ['d2', 'd4', 'e1', 'e5', 'g1', 'g5', 'h2', 'h4'],
        ['d3', 'd5', 'e2', 'e6', 'g2', 'g6', 'h3', 'h5'],
        ['d4', 'd6', 'e3', 'e7', 'g3', 'g7', 'h4', 'h6'],
        ['d5', 'd7', 'e4', 'e8', 'g4', 'g8', 'h5', 'h7'],
        ['d6', 'd8', 'e5', 'g5', 'h6', 'h8'],
        ['d7', 'e6', 'g6', 'h7']
    ], 'g': [
        ['e2', 'f3', 'h3'],
        ['e1', 'e3', 'f4', 'h4'],
        ['e2', 'e4', 'f1', 'f5', 'h1', 'h5'],
        ['e3', 'e5', 'f2', 'f6', 'h2', 'h6'],
        ['e4', 'e6', 'f3', 'f7', 'h3', 'h7'],
        ['e5', 'e7', 'f4', 'f8', 'h4', 'h8'],
        ['e6', 'e8', 'f5', 'h5'],
        ['e7', 'f6', 'h6']
    ], 'h': [
        ['f2', 'g3'],
        ['f1', 'f3', 'g4'],
        ['f2', 'f4', 'g1', 'g5'],
        ['f3', 'f5', 'g2', 'g6'],
        ['f4', 'f6', 'g3', 'g7'],
        ['f5', 'f7', 'g4', 'g8'],
        ['f6', 'f8', 'g5'],
        ['f7', 'g6']
    ]
}

BISHOP = {
    'a': [
        ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'],
        ['b1', 'b3', 'c4', 'd5', 'e6', 'f7', 'g8'],
        ['b2', 'b4', 'c1', 'c5', 'd6', 'e7', 'f8'],
        ['b3', 'b5', 'c2', 'c6', 'd1', 'd7', 'e8'],
        ['b4', 'b6', 'c3', 'c7', 'd2', 'd8', 'e1'],
        ['b5', 'b7', 'c4', 'c8', 'd3', 'e2', 'f1'],
        ['b6', 'b8', 'c5', 'd4', 'e3', 'f2', 'g1'],
        ['b7', 'c6', 'd5', 'e4', 'f3', 'g2', 'h1']
    ], 'b': [
        ['a2', 'c2', 'd3', 'e4', 'f5', 'g6', 'h7'],
        ['a1', 'a3', 'c1', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'],
        ['a2', 'a4', 'c2', 'c4', 'd1', 'd5', 'e6', 'f7', 'g8'],
        ['a3', 'a5', 'c3', 'c5', 'd2', 'd6', 'e1', 'e7', 'f8'],
        ['a4', 'a6', 'c4', 'c6', 'd3', 'd7', 'e2', 'e8', 'f1'],
        ['a5', 'a7', 'c5', 'c7', 'd4', 'd8', 'e3', 'f2', 'g1'],
        ['a6', 'a8', 'c6', 'c8', 'd5', 'e4', 'f3', 'g2', 'h1'],
        ['a7', 'c7', 'd6', 'e5', 'f4', 'g3', 'h2'],
    ],
    'c': [
        ['a3', 'b2', 'd2', 'e3', 'f4', 'g5', 'h6'],
        ['a4', 'b1', 'b3', 'd1', 'd3', 'e4', 'f5', 'g6', 'h7'],
        ['a1', 'a5', 'b2', 'b4', 'd2', 'd4', 'e1', 'e5', 'f6', 'g7', 'h8'],
        ['a2', 'a6', 'b3', 'b5', 'd3', 'd5', 'e2', 'e6', 'f1', 'f7', 'g8'],
        ['a3', 'a7', 'b4', 'b6', 'd4', 'd6', 'e3', 'e7', 'f2', 'f8', 'g1'],
        ['a4', 'a8', 'b5', 'b7', 'd5', 'd7', 'e4', 'e8', 'f3', 'g2', 'h1'],
        ['a5', 'b6', 'b8', 'd6', 'd8', 'e5', 'f4', 'g3', 'h2'],
        ['a6', 'b7', 'd7', 'e6', 'f5', 'g4', 'h3'],
    ],
    'd': [
        ['a4', 'b3', 'c2', 'e2', 'f3', 'g4', 'h5'],
        ['a5', 'b4', 'c1', 'c3', 'e1', 'e3', 'f4', 'g5', 'h6'],
        ['a6', 'b1', 'b5', 'c2', 'c4', 'e2', 'e4', 'f1', 'f5', 'g6', 'h7'],
        ['a1', 'a7', 'b2', 'b6', 'c3', 'c5', 'e3', 'e5', 'f2', 'f6', 'g1', 'g7', 'h8'],
        ['a2', 'a8', 'b3', 'b7', 'c4', 'c6', 'e4', 'e6', 'f3', 'f7', 'g2', 'g8', 'h1'],
        ['a3', 'b4', 'b8', 'c5', 'c7', 'e5', 'e7', 'f4', 'f8', 'g3', 'h2'],
        ['a4', 'b5', 'c6', 'c8', 'e6', 'e8', 'f5', 'g4', 'h3'],
        ['a5', 'b6', 'c7', 'e7', 'f6', 'g5', 'h4'],
    ],
    'e': [
        ['a5', 'b4', 'c3', 'd2', 'f2', 'g3', 'h4'],
        ['a6', 'b5', 'c4', 'd1', 'd3', 'f1', 'f3', 'g4', 'h5'],
        ['a7', 'b6', 'c1', 'c5', 'd2', 'd4', 'f2', 'f4', 'g1', 'g5', 'h6'],
        ['a8', 'b1', 'b7', 'c2', 'c6', 'd3', 'd5', 'f3', 'f5', 'g2', 'g6', 'h1', 'h7'],
        ['a1', 'b2', 'b8', 'c3', 'c7', 'd4', 'd6', 'f4', 'f6', 'g3', 'g7', 'h2', 'h8'],
        ['a2', 'b3', 'c4', 'c8', 'd5', 'd7', 'f5', 'f7', 'g4', 'g8', 'h3'],
        ['a3', 'b4', 'c5', 'd6', 'd8', 'f6', 'f8', 'g5', 'h4'],
        ['a4', 'b5', 'c6', 'd7', 'f7', 'g6', 'h5'],
    ],
    'f': [
        ['a6', 'b5', 'c4', 'd3', 'e2', 'g2', 'h3'],
        ['a7', 'b6', 'c5', 'd4', 'e1', 'e3', 'g1', 'g3', 'h4'],
        ['a8', 'b7', 'c6', 'd1', 'd5', 'e2', 'e4', 'g2', 'g4', 'h1', 'h5'],
        ['b8', 'c1', 'c7', 'd2', 'd6', 'e3', 'e5', 'g3', 'g5', 'h2', 'h6'],
        ['b1', 'c2', 'c8', 'd3', 'd7', 'e4', 'e6', 'g4', 'g6', 'h3', 'h7'],
        ['a1', 'b2', 'c3', 'd4', 'd8', 'e5', 'e7', 'g5', 'g7', 'h4', 'h8'],
        ['a2', 'b3', 'c4', 'd5', 'e6', 'e8', 'g6', 'g8', 'h5'],
        ['a3', 'b4', 'c5', 'd6', 'e7', 'g7', 'h6'],
    ],
    'g': [
        ['a7', 'b6', 'c5', 'd4', 'e3', 'f2', 'h2'],
        ['a8', 'b7', 'c6', 'd5', 'e4', 'f1', 'f3', 'h1', 'h3'],
        ['b8', 'c7', 'd6', 'e1', 'e5', 'f2', 'f4', 'h2', 'h4'],
        ['c8', 'd1', 'd7', 'e2', 'e6', 'f3', 'f5', 'h3', 'h5'],
        ['c1', 'd2', 'd8', 'e3', 'e7', 'f4', 'f6', 'h4', 'h6'],
        ['b1', 'c2', 'd3', 'e4', 'e8', 'f5', 'f7', 'h5', 'h7'],
        ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'f8', 'h6', 'h8'],
        ['a2', 'b3', 'c4', 'd5', 'e6', 'f7', 'g8'],
    ],
    'h': [
        ['a8', 'b7', 'c6', 'd5', 'e4', 'f3', 'g2'],
        ['b8', 'c7', 'd6', 'e5', 'f4', 'g1', 'g3'],
        ['c8', 'd7', 'e6', 'f1', 'f5', 'g2', 'g4'],
        ['d8', 'e1', 'e7', 'f2', 'f6', 'g3', 'g5'],
        ['d1', 'e2', 'e8', 'f3', 'f7', 'g4', 'g6'],
        ['c1', 'd2', 'e3', 'f4', 'f8', 'g5', 'g7'],
        ['b1', 'c2', 'd3', 'e4', 'f5', 'g6', 'g8'],
        ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7'],
    ]
}

ROOK = {
    'a': [
        ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],
        ['a1', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
        ['a1', 'a2', 'a4', 'a5', 'a6', 'a7', 'a8', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
        ['a1', 'a2', 'a3', 'a5', 'a6', 'a7', 'a8', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
        ['a1', 'a2', 'a3', 'a4', 'a6', 'a7', 'a8', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
        ['a1', 'a2', 'a3', 'a4', 'a5', 'a7', 'a8', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
        ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a8', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
        ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']
    ], 'b': [
        ['b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'a1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],
        ['b1', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'a2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
        ['b1', 'b2', 'b4', 'b5', 'b6', 'b7', 'b8', 'a3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
        ['b1', 'b2', 'b3', 'b5', 'b6', 'b7', 'b8', 'a4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
        ['b1', 'b2', 'b3', 'b4', 'b6', 'b7', 'b8', 'a5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
        ['b1', 'b2', 'b3', 'b4', 'b5', 'b7', 'b8', 'a6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
        ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b8', 'a7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
        ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'a8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']
    ], 'c': [
        ['c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'a1', 'b1', 'd1', 'e1', 'f1', 'g1', 'h1'],
        ['c1', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'a2', 'b2', 'd2', 'e2', 'f2', 'g2', 'h2'],
        ['c1', 'c2', 'c4', 'c5', 'c6', 'c7', 'c8', 'a3', 'b3', 'd3', 'e3', 'f3', 'g3', 'h3'],
        ['c1', 'c2', 'c3', 'c5', 'c6', 'c7', 'c8', 'a4', 'b4', 'd4', 'e4', 'f4', 'g4', 'h4'],
        ['c1', 'c2', 'c3', 'c4', 'c6', 'c7', 'c8', 'a5', 'b5', 'd5', 'e5', 'f5', 'g5', 'h5'],
        ['c1', 'c2', 'c3', 'c4', 'c5', 'c7', 'c8', 'a6', 'b6', 'd6', 'e6', 'f6', 'g6', 'h6'],
        ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c8', 'a7', 'b7', 'd7', 'e7', 'f7', 'g7', 'h7'],
        ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'a8', 'b8', 'd8', 'e8', 'f8', 'g8', 'h8']
    ], 'd': [
        ['d2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'a1', 'b1', 'c1', 'e1', 'f1', 'g1', 'h1'],
        ['d1', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'a2', 'b2', 'c2', 'e2', 'f2', 'g2', 'h2'],
        ['d1', 'd2', 'd4', 'd5', 'd6', 'd7', 'd8', 'a3', 'b3', 'c3', 'e3', 'f3', 'g3', 'h3'],
        ['d1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8', 'a4', 'b4', 'c4', 'e4', 'f4', 'g4', 'h4'],
        ['d1', 'd2', 'd3', 'd4', 'd6', 'd7', 'd8', 'a5', 'b5', 'c5', 'e5', 'f5', 'g5', 'h5'],
        ['d1', 'd2', 'd3', 'd4', 'd5', 'd7', 'd8', 'a6', 'b6', 'c6', 'e6', 'f6', 'g6', 'h6'],
        ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd8', 'a7', 'b7', 'c7', 'e7', 'f7', 'g7', 'h7'],
        ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'a8', 'b8', 'c8', 'e8', 'f8', 'g8', 'h8']
    ], 'e': [
        ['e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'a1', 'b1', 'c1', 'd1', 'f1', 'g1', 'h1'],
        ['e1', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'a2', 'b2', 'c2', 'd2', 'f2', 'g2', 'h2'],
        ['e1', 'e2', 'e4', 'e5', 'e6', 'e7', 'e8', 'a3', 'b3', 'c3', 'd3', 'f3', 'g3', 'h3'],
        ['e1', 'e2', 'e3', 'e5', 'e6', 'e7', 'e8', 'a4', 'b4', 'c4', 'd4', 'f4', 'g4', 'h4'],
        ['e1', 'e2', 'e3', 'e4', 'e6', 'e7', 'e8', 'a5', 'b5', 'c5', 'd5', 'f5', 'g5', 'h5'],
        ['e1', 'e2', 'e3', 'e4', 'e5', 'e7', 'e8', 'a6', 'b6', 'c6', 'd6', 'f6', 'g6', 'h6'],
        ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e8', 'a7', 'b7', 'c7', 'd7', 'f7', 'g7', 'h7'],
        ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'a8', 'b8', 'c8', 'd8', 'f8', 'g8', 'h8']
    ], 'f': [
        ['f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'a1', 'b1', 'c1', 'd1', 'e1', 'g1', 'h1'],
        ['f1', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'a2', 'b2', 'c2', 'd2', 'e2', 'g2', 'h2'],
        ['f1', 'f2', 'f4', 'f5', 'f6', 'f7', 'f8', 'a3', 'b3', 'c3', 'd3', 'e3', 'g3', 'h3'],
        ['f1', 'f2', 'f3', 'f5', 'f6', 'f7', 'f8', 'a4', 'b4', 'c4', 'd4', 'e4', 'g4', 'h4'],
        ['f1', 'f2', 'f3', 'f4', 'f6', 'f7', 'f8', 'a5', 'b5', 'c5', 'd5', 'e5', 'g5', 'h5'],
        ['f1', 'f2', 'f3', 'f4', 'f5', 'f7', 'f8', 'a6', 'b6', 'c6', 'd6', 'e6', 'g6', 'h6'],
        ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f8', 'a7', 'b7', 'c7', 'd7', 'e7', 'g7', 'h7'],
        ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'a8', 'b8', 'c8', 'd8', 'e8', 'g8', 'h8']
    ], 'g': [
        ['g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'h1'],
        ['g1', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'h2'],
        ['g1', 'g2', 'g4', 'g5', 'g6', 'g7', 'g8', 'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'h3'],
        ['g1', 'g2', 'g3', 'g5', 'g6', 'g7', 'g8', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'h4'],
        ['g1', 'g2', 'g3', 'g4', 'g6', 'g7', 'g8', 'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'h5'],
        ['g1', 'g2', 'g3', 'g4', 'g5', 'g7', 'g8', 'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'h6'],
        ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g8', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'h7'],
        ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'h8']
    ], 'h': [
        ['h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1'],
        ['h1', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2'],
        ['h1', 'h2', 'h4', 'h5', 'h6', 'h7', 'h8', 'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3'],
        ['h1', 'h2', 'h3', 'h5', 'h6', 'h7', 'h8', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4'],
        ['h1', 'h2', 'h3', 'h4', 'h6', 'h7', 'h8', 'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5'],
        ['h1', 'h2', 'h3', 'h4', 'h5', 'h7', 'h8', 'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6'],
        ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h8', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7'],
        ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8']
    ]                
}

QUEEN = {
    'a': [
        ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'c1', 'c3', 'd1', 'd4', 'e1', 'e5', 'f1', 'f6', 'g1', 'g7', 'h1', 'h8'],
        ['a1', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'c2', 'c4', 'd2', 'd5', 'e2', 'e6', 'f2', 'f7', 'g2', 'g8', 'h2'],
        ['a1', 'a2', 'a4', 'a5', 'a6', 'a7', 'a8', 'b2', 'b3', 'b4', 'c1', 'c3', 'c5', 'd3', 'd6', 'e3', 'e7', 'f3', 'f8', 'g3', 'h3'],
        ['a1', 'a2', 'a3', 'a5', 'a6', 'a7', 'a8', 'b3', 'b4', 'b5', 'c2', 'c4', 'c6', 'd1', 'd4', 'd7', 'e4', 'e8', 'f4', 'g4', 'h4'],
        ['a1', 'a2', 'a3', 'a4', 'a6', 'a7', 'a8', 'b4', 'b5', 'b6', 'c3', 'c5', 'c7', 'd2', 'd5', 'd8', 'e1', 'e5', 'f5', 'g5', 'h5'],
        ['a1', 'a2', 'a3', 'a4', 'a5', 'a7', 'a8', 'b5', 'b6', 'b7', 'c4', 'c6', 'c8', 'd3', 'd6', 'e2', 'e6', 'f1', 'f6', 'g6', 'h6'],
        ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a8', 'b6', 'b7', 'b8', 'c5', 'c7', 'd4', 'd7', 'e3', 'e7', 'f2', 'f7', 'g1', 'g7', 'h7'],
        ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'b7', 'b8', 'c6', 'c8', 'd5', 'd8', 'e4', 'e8', 'f3', 'f8', 'g2', 'g8', 'h1', 'h8']
    ],
    'b': [
        ['a1', 'a2', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'd1', 'd3', 'e1', 'e4', 'f1', 'f5', 'g1', 'g6', 'h1', 'h7'],
        ['a1', 'a2', 'a3', 'b1', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'd2', 'd4', 'e2', 'e5', 'f2', 'f6', 'g2', 'g7', 'h2', 'h8'],
        ['a2', 'a3', 'a4', 'b1', 'b2', 'b4', 'b5', 'b6', 'b7', 'b8', 'c2', 'c3', 'c4', 'd1', 'd3', 'd5', 'e3', 'e6', 'f3', 'f7', 'g3', 'g8', 'h3'],
        ['a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b5', 'b6', 'b7', 'b8', 'c3', 'c4', 'c5', 'd2', 'd4', 'd6', 'e1', 'e4', 'e7', 'f4', 'f8', 'g4', 'h4'],
        ['a4', 'a5', 'a6', 'b1', 'b2', 'b3', 'b4', 'b6', 'b7', 'b8', 'c4', 'c5', 'c6', 'd3', 'd5', 'd7', 'e2', 'e5', 'e8', 'f1', 'f5', 'g5', 'h5'],
        ['a5', 'a6', 'a7', 'b1', 'b2', 'b3', 'b4', 'b5', 'b7', 'b8', 'c5', 'c6', 'c7', 'd4', 'd6', 'd8', 'e3', 'e6', 'f2', 'f6', 'g1', 'g6', 'h6'],
        ['a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b8', 'c6', 'c7', 'c8', 'd5', 'd7', 'e4', 'e7', 'f3', 'f7', 'g2', 'g7', 'h1', 'h7'],
        ['a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'c7', 'c8', 'd6', 'd8', 'e5', 'e8', 'f4', 'f8', 'g3', 'g8', 'h2', 'h8']
    ],
    'c': [
        ['a1', 'a3', 'b1', 'b2', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'e1', 'e3', 'f1', 'f4', 'g1', 'g5', 'h1', 'h6'],
        ['a2', 'a4', 'b1', 'b2', 'b3', 'c1', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd2', 'd3', 'd4', 'e2', 'e4', 'f2', 'f5', 'g2', 'g6', 'h2', 'h7'],
        ['a1', 'a3', 'a5', 'b2', 'b3', 'b4', 'c1', 'c2', 'c4', 'c5', 'c6', 'c7', 'c8', 'd2', 'd3', 'd4', 'e1', 'e3', 'e5', 'f3', 'f6', 'g3', 'g7', 'h3', 'h8'],
        ['a2', 'a4', 'a6', 'b3', 'b4', 'b5', 'c1', 'c2', 'c3', 'c5', 'c6', 'c7', 'c8', 'd3', 'd4', 'd5', 'e2', 'e4', 'e6', 'f1', 'f4', 'f7', 'g4', 'g8', 'h4'],
        ['a3', 'a5', 'a7', 'b4', 'b5', 'b6', 'c1', 'c2', 'c3', 'c4', 'c6', 'c7', 'c8', 'd4', 'd5', 'd6', 'e3', 'e5', 'e7', 'f2', 'f5', 'f8', 'g1', 'g5', 'h5'],
        ['a4', 'a6', 'a8', 'b5', 'b6', 'b7', 'c1', 'c2', 'c3', 'c4', 'c5', 'c7', 'c8', 'd5', 'd6', 'd7', 'e4', 'e6', 'e8', 'f3', 'f6', 'g2', 'g6', 'h1', 'h6'],
        ['a5', 'a7', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c8', 'd6', 'd7', 'd8', 'e5', 'e7', 'f4', 'f7', 'g3', 'g7', 'h2', 'h7'],
        ['a6', 'a8', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'd7', 'd8', 'e6', 'e8', 'f5', 'f8', 'g4', 'g8', 'h3', 'h8']

    ],
    'd': [
        ['a1', 'a4', 'b1', 'b3', 'c1', 'c2', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'f1', 'f3', 'g1', 'g4', 'h1', 'h5'],
        ['a2', 'a5', 'b2', 'b4', 'c1', 'c2', 'c3', 'd1', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'f2', 'f4', 'g2', 'g5', 'h2', 'h6'],
        ['a3', 'a6', 'b1', 'b3', 'b5', 'c2', 'c3', 'c4', 'd1', 'd2', 'd4', 'd5', 'd6', 'd7', 'd8', 'e2', 'e3', 'e4', 'f1', 'f3', 'f5', 'g3', 'g6', 'h3', 'h7'],
        ['a1', 'a4', 'a7', 'b2', 'b4', 'b6', 'c3', 'c4', 'c5', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8', 'e3', 'e4', 'e5', 'f2', 'f4', 'f6', 'g1', 'g4', 'g7', 'h4', 'h8'],
        ['a2', 'a5', 'a8', 'b3', 'b5', 'b7', 'c4', 'c5', 'c6', 'd1', 'd2', 'd3', 'd4', 'd6', 'd7', 'd8', 'e4', 'e5', 'e6', 'f3', 'f5', 'f7', 'g2', 'g5', 'g8', 'h1', 'h5'],
        ['a3', 'a6', 'b4', 'b6', 'b8', 'c5', 'c6', 'c7', 'd1', 'd2', 'd3', 'd4', 'd5', 'd7', 'd8', 'e5', 'e6', 'e7', 'f4' ,'f6', 'f8', 'g3', 'g6', 'h2', 'h6'],
        ['a4', 'a7', 'b5', 'b7', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd8', 'e6', 'e7', 'e8', 'f5', 'f7', 'g4', 'g7', 'h3', 'h7'],
        ['a5', 'a8', 'b6', 'b8', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'e7', 'e8', 'f6', 'f8', 'g5', 'g8', 'h4', 'h8']
    ],
    'e': [
        ['a1', 'a5', 'b1', 'b4', 'c1', 'c3', 'd1', 'd2', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'g1', 'g3', 'h1', 'h5'],
        ['a2', 'a6', 'b2', 'b5', 'c2', 'c4', 'd1', 'd2', 'd3', 'e1', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'g2', 'g4', 'h2', 'h5'],
        ['a3', 'a7', 'b3', 'b6', 'c1', 'c3', 'c5', 'd2', 'd3', 'd4', 'e1', 'e2', 'e4', 'e5', 'e6', 'e7', 'e8', 'f2', 'f3', 'f4', 'g1', 'g3', 'g5', 'h3', 'h6'],
        ['a4', 'a8', 'b1', 'b4', 'b7', 'c2', 'c4', 'c6', 'd3', 'd4', 'd5', 'e1', 'e2', 'e3', 'e5', 'e6', 'e7', 'e8', 'f3', 'f4', 'f5', 'g2', 'g4', 'g6', 'h1', 'h4', 'h7'],
        ['a1', 'a5', 'b2', 'b5', 'b8', 'c3', 'c5', 'c7', 'd4', 'd5', 'd6', 'e1', 'e2', 'e3', 'e4', 'e6', 'e7', 'e8', 'f4', 'f5', 'f6', 'g3', 'g5', 'g7', 'h2', 'h5', 'h8'],
        ['a2', 'a6', 'b3', 'b6', 'c4', 'c6', 'c8', 'd5', 'd6', 'd7', 'e1', 'e2', 'e3', 'e4', 'e5', 'e7', 'e8', 'f5', 'f6', 'f7', 'g4', 'g6', 'g8', 'h3', 'h6'],
        ['a3', 'a7', 'b4', 'b7', 'c5', 'c7', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e8', 'f6', 'f7', 'f8', 'g5', 'g7', 'h4', 'h7'],
        ['a4', 'a8', 'b5', 'b8', 'c6', 'c8', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'f7', 'f8', 'g6', 'g8', 'h5', 'h8'] 
    ],
    'f': [
        ['a1', 'a6', 'b1', 'b5', 'c1', 'c4', 'd1', 'd3', 'e1', 'e2', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'h1', 'h3'],
        ['a2', 'a7', 'b2', 'b6', 'c2', 'c5', 'd2', 'd4', 'e1', 'e2', 'e3', 'f1', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'h2', 'h4'],
        ['a3', 'a8', 'b3', 'b7', 'c3', 'c6', 'd1', 'd3', 'd5', 'e2', 'e3', 'e4', 'f1', 'f2', 'f4', 'f5', 'f6', 'f7', 'f8', 'g2', 'g3', 'g4', 'h1', 'h3', 'h5'],
        ['a4', 'b4', 'b8', 'c1', 'c4', 'c7', 'd2', 'd4', 'd6', 'e3', 'e4', 'e5', 'f1', 'f2', 'f3', 'f5', 'f6', 'f7', 'f8', 'g3', 'g4', 'g5', 'h2', 'h4', 'h6'],
        ['a5', 'b1', 'b5', 'c2', 'c5', 'c8', 'd3', 'd5', 'd7', 'e4', 'e5', 'e6', 'f1', 'f2', 'f3', 'f4', 'f6', 'f7', 'f8', 'g4', 'g5', 'g6', 'h3', 'h5', 'h7'],
        ['a1', 'a6', 'b2', 'b6', 'c3', 'c6', 'd4', 'd6', 'd8', 'e5', 'e6', 'e7', 'f1', 'f2', 'f3', 'f4', 'f5', 'f7', 'f8', 'g5', 'g6', 'g7', 'h4', 'h6', 'h8'],
        ['a2', 'a7', 'b3', 'b7', 'c4', 'c7', 'd5', 'd7', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f8', 'g6', 'g7', 'g8', 'h5', 'h7'],
        ['a3', 'a8', 'b4', 'b8', 'c5', 'c8', 'd6', 'd8', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'g7', 'g8', 'h6', 'h8']
    ],
    'g': [
        ['a1', 'a7', 'b1', 'b6', 'c1', 'c5', 'd1', 'd4', 'e1', 'e3', 'f1', 'f2', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2'],
        ['a2', 'a8', 'b2', 'b7', 'c2', 'c6', 'd2', 'd5', 'e2', 'e4', 'f1', 'f2', 'f3', 'g1', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3'],
        ['a3', 'b3', 'b8', 'c3', 'c7', 'd3', 'd6', 'e1', 'e3', 'e5', 'f2', 'f3', 'f4', 'g1', 'g2', 'g4', 'g5', 'g6', 'g7', 'g8', 'h2', 'h3', 'h4'],
        ['a4', 'b4', 'c4', 'c8', 'd1', 'd4', 'd7', 'e2', 'e4', 'e6', 'f3', 'f4', 'f5', 'g1', 'g2', 'g3', 'g5', 'g6', 'g7', 'g8', 'h3', 'h4', 'h5'],
        ['a5', 'b5', 'c1', 'c5', 'd2', 'd5', 'd8', 'e3', 'e5', 'e7', 'f4', 'f5', 'f6', 'g1', 'g2', 'g3', 'g4', 'g6', 'g7', 'g8', 'h4', 'h5', 'h6'],
        ['a6', 'b1', 'b6', 'c2', 'c6', 'd3', 'd6', 'e4', 'e6', 'e8', 'f5', 'f6', 'f7', 'g1', 'g2', 'g3', 'g4', 'g5', 'g7', 'g8', 'h5', 'h6', 'h7'],
        ['a1', 'a7', 'b2', 'b7', 'c3', 'c7', 'd4', 'd7', 'e5', 'e7', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g8', 'h6', 'h7', 'h8'],
        ['a2', 'a8', 'b3', 'b8', 'c4', 'c8', 'd5', 'd8', 'e6', 'e8', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'h7', 'h8']

    ],
    'h': [
        ['a1', 'a8', 'b1', 'b7', 'c1', 'c6', 'd1', 'd5', 'e1', 'e4', 'f1', 'f3', 'g1', 'g2', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
        ['a2', 'b2', 'b8', 'c2', 'c7', 'd2', 'd6', 'e2', 'e5', 'f2', 'f4', 'g1', 'g2', 'g3', 'h1', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
        ['a3', 'b3', 'c3', 'c8', 'd3', 'd7', 'e3', 'e6', 'f1', 'f3', 'f5', 'g2', 'g3', 'g4', 'h1', 'h2', 'h4', 'h5', 'h6', 'h7', 'h8'],
        ['a4', 'b4', 'c4', 'd4', 'd8', 'e1', 'e4', 'e7', 'f2', 'f4', 'f6', 'g3', 'g4', 'g5', 'h1', 'h2', 'h3', 'h5', 'h6', 'h7', 'h8'],
        ['a5', 'b5', 'c5', 'd1', 'd5', 'e2', 'e5', 'e8', 'f3', 'f5', 'f7', 'g4', 'g5', 'g6', 'h1', 'h2', 'h3', 'h4', 'h6', 'h7', 'h8'],
        ['a6', 'b6', 'c1', 'c6', 'd2', 'd6', 'e3', 'e6', 'f4', 'f6', 'f8', 'g5', 'g6', 'g7', 'h1', 'h2', 'h3', 'h4', 'h5', 'h7', 'h8'],
        ['a7', 'b1', 'b7', 'c2', 'c7', 'd3', 'd7', 'e4', 'e7', 'f5', 'f7', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h8'],
        ['a1', 'a8', 'b2', 'b8', 'c3', 'c8', 'd4', 'd8', 'e5', 'e8', 'f6', 'f8', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7']
    ]
}

KING = {
    'a': [
        ['a2', 'b1', 'b2'],
        ['a1', 'a3', 'b1', 'b2', 'b3'],
        ['a2', 'a4', 'b2', 'b3', 'b4'],
        ['a3', 'a5', 'b3', 'b4', 'b5'],
        ['a4', 'a6', 'b4', 'b5', 'b6'],
        ['a5', 'a7', 'b5', 'b6', 'b7'],
        ['a6', 'a8', 'b6', 'b7', 'b8'],
        ['a7', 'b7', 'b8']
    ],
    'b': [
        ['a1', 'a2', 'b2', 'c1', 'c2'],
        ['a1', 'a2', 'a3', 'b1', 'b3', 'c1', 'c2', 'c3'],
        ['a2', 'a3', 'a4', 'b2', 'b4', 'c2', 'c3', 'c4'],
        ['a3', 'a4', 'a5', 'b3', 'b5', 'c3', 'c4', 'c5'],
        ['a4', 'a5', 'a6', 'b4', 'b6', 'c4', 'c5', 'c6'],
        ['a5', 'a6', 'a7', 'b5', 'b7', 'c5', 'c6', 'c7'],
        ['a6', 'a7', 'a8', 'b6', 'b8', 'c6', 'c7', 'c8'],
        ['a7', 'a8', 'b7', 'c7', 'c8']
    ],
    'c': [
        ['b1', 'b2', 'c2', 'd1', 'd2'],
        ['b1', 'b2', 'b3', 'c1', 'c3', 'd1', 'd2', 'd3'],
        ['b2', 'b3', 'b4', 'c2', 'c4', 'd2', 'd3', 'd4'],
        ['b3', 'b4', 'b5', 'c3', 'c5', 'd3', 'd4', 'd5'],
        ['b4', 'b5', 'b6', 'c4', 'c6', 'd4', 'd5', 'd6'],
        ['b5', 'b6', 'b7', 'c5', 'c7', 'd5', 'd6', 'd7'],
        ['b6', 'b7', 'b8', 'c6', 'c8', 'd6', 'd7', 'd8'],
        ['b7', 'b8', 'c7', 'd7', 'd8']
    ],
    'd': [
        ['c1', 'c2', 'd2', 'e1', 'e2'],
        ['c1', 'c2', 'c3', 'd1', 'd3', 'e1', 'e2', 'e3'],
        ['c2', 'c3', 'c4', 'd2', 'd4', 'e2', 'e3', 'e4'],
        ['c3', 'c4', 'c5', 'd3', 'd5', 'e3', 'e4', 'e5'],
        ['c4', 'c5', 'c6', 'd4', 'd6', 'e4', 'e5', 'e6'],
        ['c5', 'c6', 'c7', 'd5', 'd7', 'e5', 'e6', 'e7'],
        ['c6', 'c7', 'c8', 'd6', 'd8', 'e6', 'e7', 'e8'],
        ['c7', 'c8', 'd7', 'e7', 'e8']
    ],
    'e': [
        ['d1', 'd2', 'e2', 'f1', 'f2'],
        ['d1', 'd2', 'd3', 'e1', 'e3', 'f1', 'f2', 'f3'],
        ['d2', 'd3', 'd4', 'e2', 'e4', 'f2', 'f3', 'f4'],
        ['d3', 'd4', 'd5', 'e3', 'e5', 'f3', 'f4', 'f5'],
        ['d4', 'd5', 'd6', 'e4', 'e6', 'f4', 'f5', 'f6'],
        ['d5', 'd6', 'd7', 'e5', 'e7', 'f5', 'f6', 'f7'],
        ['d6', 'd7', 'd8', 'e6', 'e8', 'f6', 'f7', 'f8'],
        ['d7', 'd8', 'e7', 'f7', 'f8']
    ],
    'f': [
        ['e1', 'e2', 'f2', 'g1', 'g2'],
        ['e1', 'e2', 'e3', 'f1', 'f3', 'g1', 'g2', 'g3'],
        ['e2', 'e3', 'e4', 'f2', 'f4', 'g2', 'g3', 'g4'],
        ['e3', 'e4', 'e5', 'f3', 'f5', 'g3', 'g4', 'g5'],
        ['e4', 'e5', 'e6', 'f4', 'f6', 'g4', 'g5', 'g6'],
        ['e5', 'e6', 'e7', 'f5', 'f7', 'g5', 'g6', 'g7'],
        ['e6', 'e7', 'e8', 'f6', 'f8', 'g6', 'g7', 'g8'],
        ['e7', 'e8', 'f7', 'g7', 'g8']
    ],
    'g': [
        ['f1', 'f2', 'g2', 'h1', 'h2'],
        ['f1', 'f2', 'f3', 'g1', 'g3', 'h1', 'h2', 'h3'],
        ['f2', 'f3', 'f4', 'g2', 'g4', 'h2', 'h3', 'h4'],
        ['f3', 'f4', 'f5', 'g3', 'g5', 'h3', 'h4', 'h5'],
        ['f4', 'f5', 'f6', 'g4', 'g6', 'h4', 'h5', 'h6'],
        ['f5', 'f6', 'f7', 'g5', 'g7', 'h5', 'h6', 'h7'],
        ['f6', 'f7', 'f8', 'g6', 'g8', 'h6', 'h7', 'h8'],
        ['f7', 'f8', 'g7', 'h7', 'h8']
    ],
    'h': [
        ['g1', 'g2', 'h2'],
        ['g1', 'g2', 'g3', 'h1', 'h3'],
        ['g2', 'g3', 'g4', 'h2', 'h4'],
        ['g3', 'g4', 'g5', 'h3', 'h5'],
        ['g4', 'g5', 'g6', 'h4', 'h6'],
        ['g5', 'g6', 'g7', 'h5', 'h7'],
        ['g6', 'g7', 'g8', 'h6', 'h8'],
        ['g7', 'g8', 'h7']
    ]
}