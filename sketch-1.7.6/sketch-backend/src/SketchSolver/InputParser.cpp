/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton implementation for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "2.3"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 1

/* Using locations.  */
#define YYLSP_NEEDED 0



/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     T_dbl = 258,
     T_int = 259,
     T_bool = 260,
     T_ident = 261,
     T_OutIdent = 262,
     T_NativeCode = 263,
     T_string = 264,
     T_true = 265,
     T_false = 266,
     T_vartype = 267,
     T_rightAC = 268,
     T_leftAC = 269,
     T_rightTC = 270,
     T_leftTC = 271,
     T_leftAR = 272,
     T_rightAR = 273,
     T_arrow = 274,
     T_twoS = 275,
     T_ppls = 276,
     T_mmns = 277,
     T_eq = 278,
     T_neq = 279,
     T_and = 280,
     T_or = 281,
     T_For = 282,
     T_ge = 283,
     T_le = 284,
     T_fixes = 285,
     T_File = 286,
     T_Native = 287,
     T_NativeMethod = 288,
     T_Sketches = 289,
     T_new = 290,
     T_Typedef = 291,
     T_def = 292,
     T_mdldef = 293,
     T_Min = 294,
     T_sp = 295,
     T_assert = 296,
     T_assume = 297,
     T_hassert = 298,
     T_equals = 299,
     T_replace = 300,
     T_eof = 301
   };
#endif
/* Tokens.  */
#define T_dbl 258
#define T_int 259
#define T_bool 260
#define T_ident 261
#define T_OutIdent 262
#define T_NativeCode 263
#define T_string 264
#define T_true 265
#define T_false 266
#define T_vartype 267
#define T_rightAC 268
#define T_leftAC 269
#define T_rightTC 270
#define T_leftTC 271
#define T_leftAR 272
#define T_rightAR 273
#define T_arrow 274
#define T_twoS 275
#define T_ppls 276
#define T_mmns 277
#define T_eq 278
#define T_neq 279
#define T_and 280
#define T_or 281
#define T_For 282
#define T_ge 283
#define T_le 284
#define T_fixes 285
#define T_File 286
#define T_Native 287
#define T_NativeMethod 288
#define T_Sketches 289
#define T_new 290
#define T_Typedef 291
#define T_def 292
#define T_mdldef 293
#define T_Min 294
#define T_sp 295
#define T_assert 296
#define T_assume 297
#define T_hassert 298
#define T_equals 299
#define T_replace 300
#define T_eof 301




/* Copy the first part of user declarations.  */
#line 1 "InputParser/InputParser.yy"


using namespace std;

BooleanDAGCreator* currentBD;
stack<string> namestack;
vartype Gvartype;
string tupleName;

bool isModel;




#ifdef CONST
#undef CONST
#endif


#define YY_DECL int yylex (YYSTYPE* yylval, yyscan_t yyscanner)
extern int yylex (YYSTYPE* yylval, yyscan_t yyscanner);



/* Enabling traces.  */
#ifndef YYDEBUG
# define YYDEBUG 1
#endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* Enabling the token table.  */
#ifndef YYTOKEN_TABLE
# define YYTOKEN_TABLE 0
#endif

#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
#line 30 "InputParser/InputParser.yy"
{
	int intConst;
	bool boolConst;
	std::string* strConst;
	double doubleConst;		
	std::list<int>* iList;
	list<bool_node*>* nList;
	list<string*>* sList;
	vartype variableType;
	BooleanDAG* bdag;
	bool_node* bnode;
  OutType* otype;
  vector<OutType*>* tVector;
  vector<string>* sVector;
}
/* Line 193 of yacc.c.  */
#line 228 "InputParser.cpp"
	YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif



/* Copy the second part of user declarations.  */


/* Line 216 of yacc.c.  */
#line 241 "InputParser.cpp"

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#elif (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
typedef signed char yytype_int8;
#else
typedef short int yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(msgid) dgettext ("bison-runtime", msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(msgid) msgid
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(e) ((void) (e))
#else
# define YYUSE(e) /* empty */
#endif

/* Identity function, used to suppress warnings about constant conditions.  */
#ifndef lint
# define YYID(n) (n)
#else
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static int
YYID (int i)
#else
static int
YYID (i)
    int i;
#endif
{
  return i;
}
#endif

#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#     ifndef _STDLIB_H
#      define _STDLIB_H 1
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's `empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (YYID (0))
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined _STDLIB_H \
       && ! ((defined YYMALLOC || defined malloc) \
	     && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef _STDLIB_H
#    define _STDLIB_H 1
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
	 || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss;
  YYSTYPE yyvs;
  };

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

/* Copy COUNT objects from FROM to TO.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(To, From, Count) \
      __builtin_memcpy (To, From, (Count) * sizeof (*(From)))
#  else
#   define YYCOPY(To, From, Count)		\
      do					\
	{					\
	  YYSIZE_T yyi;				\
	  for (yyi = 0; yyi < (Count); yyi++)	\
	    (To)[yyi] = (From)[yyi];		\
	}					\
      while (YYID (0))
#  endif
# endif

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack)					\
    do									\
      {									\
	YYSIZE_T yynewbytes;						\
	YYCOPY (&yyptr->Stack, Stack, yysize);				\
	Stack = &yyptr->Stack;						\
	yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
	yyptr += yynewbytes / sizeof (*yyptr);				\
      }									\
    while (YYID (0))

#endif

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  5
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   511

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  71
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  37
/* YYNRULES -- Number of rules.  */
#define YYNRULES  137
/* YYNRULES -- Number of states.  */
#define YYNSTATES  357

/* YYTRANSLATE(YYLEX) -- Bison symbol number corresponding to YYLEX.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   301

#define YYTRANSLATE(YYX)						\
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[YYLEX] -- Bison symbol number corresponding to YYLEX.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,    55,     2,     2,    65,    50,    66,     2,
      59,    60,    48,    47,    58,    70,    69,    49,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    54,    63,
      51,    64,    52,    53,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,    56,     2,    57,    68,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,    61,    67,    62,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46
};

#if YYDEBUG
/* YYPRHS[YYN] -- Index of the first RHS symbol of rule number YYN in
   YYRHS.  */
static const yytype_uint16 yyprhs[] =
{
       0,     0,     3,     7,     8,    11,    14,    17,    20,    22,
      23,    27,    29,    32,    35,    38,    44,    48,    52,    59,
      66,    74,    82,    83,    90,    91,    98,   105,   112,   113,
     115,   119,   121,   123,   124,   134,   136,   142,   148,   150,
     151,   154,   160,   165,   171,   172,   175,   176,   181,   192,
     196,   200,   206,   207,   212,   218,   219,   222,   225,   226,
     229,   231,   236,   248,   253,   257,   263,   267,   273,   278,
     281,   282,   284,   288,   292,   296,   300,   304,   308,   312,
     317,   323,   328,   337,   346,   353,   357,   364,   368,   372,
     376,   380,   384,   388,   392,   396,   400,   404,   410,   411,
     414,   416,   419,   421,   423,   440,   456,   459,   462,   466,
     468,   472,   477,   483,   488,   494,   499,   504,   510,   517,
     526,   536,   547,   548,   551,   553,   557,   561,   563,   567,
     571,   575,   579,   581,   584,   586,   588,   590
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int8 yyrhs[] =
{
      72,     0,    -1,    88,    73,    46,    -1,    -1,    82,    73,
      -1,    92,    73,    -1,    90,    73,    -1,    89,    73,    -1,
       6,    -1,    -1,     6,    75,    74,    -1,     6,    -1,     6,
      76,    -1,    12,     6,    -1,     6,     6,    -1,     6,     6,
      51,   105,    52,    -1,    55,    12,     6,    -1,    55,     6,
       6,    -1,    12,    56,    48,   103,    57,     6,    -1,     6,
      56,    48,   103,    57,     6,    -1,    55,    12,    56,    48,
     103,    57,     6,    -1,    55,     6,    56,    48,   103,    57,
       6,    -1,    -1,    12,    56,   103,    57,    78,    74,    -1,
      -1,     6,    56,   103,    57,    79,    74,    -1,    55,    12,
      56,   103,    57,    76,    -1,    55,     6,    56,   103,    57,
      76,    -1,    -1,    77,    -1,    77,    58,    80,    -1,    38,
      -1,    37,    -1,    -1,    81,     6,    83,    59,    80,    60,
      61,    95,    62,    -1,    12,    -1,    12,    56,    48,   103,
      57,    -1,     6,    56,    48,   103,    57,    -1,     6,    -1,
      -1,    85,    84,    -1,    85,    12,    56,   106,    57,    -1,
       6,    59,    85,    60,    -1,     6,    59,   106,    85,    60,
      -1,    -1,    87,    86,    -1,    -1,    36,    61,    87,    62,
      -1,    45,     6,    48,     6,    44,     6,    59,   105,    60,
      63,    -1,    30,     6,    63,    -1,     6,    34,     6,    -1,
       6,    34,     6,    31,     9,    -1,    -1,    41,    93,    91,
      63,    -1,     6,    59,    94,    60,    63,    -1,    -1,     6,
      94,    -1,     9,    94,    -1,    -1,    95,    96,    -1,    63,
      -1,     6,    64,    98,    63,    -1,    65,   100,    20,    99,
      65,    56,    98,    57,    64,    98,    63,    -1,     7,    64,
      98,    63,    -1,    41,    98,    63,    -1,    41,    98,    54,
       9,    63,    -1,    43,    98,    63,    -1,    43,    98,    54,
       9,    63,    -1,    42,    98,    97,    63,    -1,    54,     9,
      -1,    -1,   101,    -1,   101,    66,   101,    -1,   101,    25,
     101,    -1,   101,    67,   101,    -1,   101,    26,   101,    -1,
     101,    68,   101,    -1,   101,    24,   101,    -1,   101,    23,
     101,    -1,   101,    17,    98,    18,    -1,   101,    69,    56,
     105,    57,    -1,   105,    56,    98,    57,    -1,     6,    56,
      56,    98,    19,    98,    57,    57,    -1,   105,    56,    56,
      98,    19,    98,    57,    57,    -1,    65,    99,    65,    56,
      98,    57,    -1,    14,    99,    13,    -1,    56,     6,    57,
      16,    99,    15,    -1,    20,    99,    20,    -1,   101,    47,
     101,    -1,   101,    49,   101,    -1,   101,    50,   101,    -1,
     101,    48,   101,    -1,   101,    70,   101,    -1,   101,    52,
     101,    -1,   101,    51,   101,    -1,   101,    28,   101,    -1,
     101,    29,   101,    -1,    98,    53,    98,    54,    98,    -1,
      -1,   101,    99,    -1,     6,    -1,     6,   100,    -1,   106,
      -1,     3,    -1,     6,    56,    48,     6,    57,    59,    99,
      60,    59,    98,    60,    56,     6,    58,   106,    57,    -1,
       6,    56,    12,    57,    59,    99,    60,    59,    98,    60,
      56,     6,    58,   106,    57,    -1,    70,   101,    -1,    55,
     101,    -1,    59,    98,    60,    -1,   107,    -1,    51,   107,
      52,    -1,    51,   107,   106,    52,    -1,    51,   107,   106,
      48,    52,    -1,    51,   107,    47,    52,    -1,    51,   107,
     106,    47,    52,    -1,    51,   107,    65,    52,    -1,    39,
      51,   107,    52,    -1,    39,    51,   107,   106,    52,    -1,
      39,    51,   107,   106,    48,    52,    -1,    40,   106,    65,
     102,    65,    51,   107,    52,    -1,    40,   106,    65,   102,
      65,    51,   107,   106,    52,    -1,    40,   106,    65,   102,
      65,    51,   107,   106,    48,    52,    -1,    -1,   102,   107,
      -1,   104,    -1,   103,    47,   104,    -1,   103,    70,   104,
      -1,   105,    -1,    59,   104,    60,    -1,   104,    48,   104,
      -1,   104,    49,   104,    -1,   104,    50,   104,    -1,   106,
      -1,    70,   106,    -1,     4,    -1,    10,    -1,    11,    -1,
       6,    -1
};

/* YYRLINE[YYN] -- source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,   129,   129,   132,   133,   134,   135,   136,   139,   155,
     155,   171,   172,   178,   191,   198,   205,   215,   221,   235,
     239,   248,   251,   251,   252,   252,   253,   254,   257,   258,
     259,   261,   261,   264,   263,   280,   288,   293,   296,   300,
     301,   305,   317,   322,   326,   327,   329,   330,   332,   338,
     342,   350,   362,   362,   374,   384,   387,   391,   397,   398,
     401,   402,   406,   433,   438,   445,   456,   465,   478,   495,
     496,   498,   499,   502,   505,   508,   511,   514,   518,   521,
     524,   532,   535,   542,   548,   562,   585,   601,   615,   619,
     623,   627,   630,   634,   638,   641,   645,   649,   660,   661,
     672,   676,   681,   684,   688,   723,   771,   774,   778,   781,
     786,   790,   798,   803,   807,   811,   815,   819,   827,   832,
     837,   846,   853,   854,   859,   860,   861,   863,   864,   865,
     866,   868,   872,   873,   876,   877,   878,   880
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || YYTOKEN_TABLE
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "T_dbl", "T_int", "T_bool", "T_ident",
  "T_OutIdent", "T_NativeCode", "T_string", "T_true", "T_false",
  "T_vartype", "T_rightAC", "T_leftAC", "T_rightTC", "T_leftTC",
  "T_leftAR", "T_rightAR", "T_arrow", "T_twoS", "T_ppls", "T_mmns", "T_eq",
  "T_neq", "T_and", "T_or", "T_For", "T_ge", "T_le", "T_fixes", "T_File",
  "T_Native", "T_NativeMethod", "T_Sketches", "T_new", "T_Typedef",
  "T_def", "T_mdldef", "T_Min", "T_sp", "T_assert", "T_assume",
  "T_hassert", "T_equals", "T_replace", "T_eof", "'+'", "'*'", "'/'",
  "'%'", "'<'", "'>'", "'?'", "':'", "'!'", "'['", "']'", "','", "'('",
  "')'", "'{'", "'}'", "';'", "'='", "'$'", "'&'", "'|'", "'^'", "'.'",
  "'-'", "$accept", "Program", "MethodList", "InList", "@1", "OutList",
  "ParamDecl", "@2", "@3", "ParamList", "Mhelp", "Method", "@4",
  "TupleType", "TupleTypeList", "TypeLine", "TypeList", "Typedef",
  "Replacement", "FixesClause", "AssertionExpr", "HLAssertion", "@5",
  "TokenList", "WorkBody", "WorkStatement", "OptionalMsg", "Expression",
  "varList", "IdentList", "Term", "ParentsList", "ConstantExpr",
  "ConstantTerm", "NegConstant", "Constant", "Ident", 0
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[YYLEX-NUM] -- Internal token number corresponding to
   token YYLEX-NUM.  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   299,   300,   301,    43,    42,    47,
      37,    60,    62,    63,    58,    33,    91,    93,    44,    40,
      41,   123,   125,    59,    61,    36,    38,   124,    94,    46,
      45
};
# endif

/* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,    71,    72,    73,    73,    73,    73,    73,    74,    75,
      74,    76,    76,    77,    77,    77,    77,    77,    77,    77,
      77,    77,    78,    77,    79,    77,    77,    77,    80,    80,
      80,    81,    81,    83,    82,    84,    84,    84,    84,    85,
      85,    85,    86,    86,    87,    87,    88,    88,    89,    90,
      91,    91,    93,    92,    92,    94,    94,    94,    95,    95,
      96,    96,    96,    96,    96,    96,    96,    96,    96,    97,
      97,    98,    98,    98,    98,    98,    98,    98,    98,    98,
      98,    98,    98,    98,    98,    98,    98,    98,    98,    98,
      98,    98,    98,    98,    98,    98,    98,    98,    99,    99,
     100,   100,   101,   101,   101,   101,   101,   101,   101,   101,
     101,   101,   101,   101,   101,   101,   101,   101,   101,   101,
     101,   101,   102,   102,   103,   103,   103,   104,   104,   104,
     104,   104,   105,   105,   106,   106,   106,   107
};

/* YYR2[YYN] -- Number of symbols composing right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     3,     0,     2,     2,     2,     2,     1,     0,
       3,     1,     2,     2,     2,     5,     3,     3,     6,     6,
       7,     7,     0,     6,     0,     6,     6,     6,     0,     1,
       3,     1,     1,     0,     9,     1,     5,     5,     1,     0,
       2,     5,     4,     5,     0,     2,     0,     4,    10,     3,
       3,     5,     0,     4,     5,     0,     2,     2,     0,     2,
       1,     4,    11,     4,     3,     5,     3,     5,     4,     2,
       0,     1,     3,     3,     3,     3,     3,     3,     3,     4,
       5,     4,     8,     8,     6,     3,     6,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     5,     0,     2,
       1,     2,     1,     1,    16,    15,     2,     2,     3,     1,
       3,     4,     5,     4,     5,     4,     4,     5,     6,     8,
       9,    10,     0,     2,     1,     3,     3,     1,     3,     3,
       3,     3,     1,     2,     1,     1,     1,     1
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint8 yydefact[] =
{
      46,     0,     0,     3,    44,     1,     0,     0,    32,    31,
      52,     0,     0,     0,     3,     3,     3,     3,     0,    55,
       0,     0,     0,     2,    33,     4,     7,     6,     5,     0,
      47,    45,    55,    55,     0,    49,     0,     0,     0,     0,
      39,    56,    57,     0,     0,    53,     0,    28,   134,   135,
     136,     0,    39,    54,    50,     0,     0,     0,     0,    29,
       0,    38,    35,    42,    40,     0,     0,     0,    14,     0,
      13,     0,     0,     0,    28,     0,     0,     0,    43,    51,
       0,     0,     0,     0,     0,     0,   124,   127,   132,     0,
       0,    17,     0,    16,     0,    30,    58,     0,     0,     0,
       0,     0,     0,     0,   133,     0,    24,     0,     0,     0,
       0,     0,    22,     0,     0,     0,     0,     0,     0,     0,
      41,     0,    15,     0,   128,   125,     0,   126,   129,   130,
     131,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    34,    60,     0,    59,    37,    36,    48,    19,
       8,    25,    18,    23,     0,    11,    27,     0,    26,     0,
       0,   103,   137,    98,    98,     0,     0,     0,     0,     0,
       0,    98,     0,     0,    71,     0,   102,   109,    70,     0,
     100,     0,     0,    21,    12,    20,     0,     0,     0,   137,
       0,     0,    98,   102,     0,     0,     0,   137,     0,   107,
       0,     0,     0,   106,   102,     0,     0,    64,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      66,   101,    98,    10,    61,    63,     0,     0,     0,     0,
      85,    99,    87,     0,   122,     0,   110,     0,     0,     0,
     108,     0,     0,     0,     0,    78,    77,    73,    75,    95,
      96,    88,    91,    89,    90,    94,    93,    72,    74,    76,
       0,    92,     0,     0,    69,    68,     0,     0,     0,     0,
       0,   116,     0,     0,   113,   115,     0,     0,   111,    98,
       0,     0,    65,    79,     0,   137,     0,    81,    67,     0,
      98,     0,     0,     0,   117,     0,   123,   114,   112,     0,
       0,    97,    80,     0,     0,     0,    98,     0,   118,     0,
      86,    84,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    82,   119,     0,    83,     0,     0,     0,     0,
     120,     0,     0,     0,   121,    62,     0,     0,     0,     0,
       0,     0,     0,     0,   105,     0,   104
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     2,    12,   151,   182,   156,    59,   132,   126,    60,
      13,    14,    39,    64,    51,    31,    18,     3,    15,    16,
      37,    17,    21,    34,   117,   145,   228,   173,   191,   181,
     174,   283,    85,    86,   175,   193,   177
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -166
static const yytype_int16 yypact[] =
{
     -29,     5,   133,   263,  -166,  -166,    34,   173,  -166,  -166,
    -166,   194,   125,   199,   263,   263,   263,   263,    -3,   153,
     139,   209,   189,  -166,  -166,  -166,  -166,  -166,  -166,   180,
    -166,  -166,   153,   153,   192,  -166,   221,   214,   251,   201,
     216,  -166,  -166,   220,   266,  -166,   244,    -2,  -166,  -166,
    -166,    22,  -166,  -166,   272,   300,    -1,     8,   176,   253,
     254,   275,   281,  -166,  -166,    50,   350,   293,   314,     2,
    -166,    15,    27,    39,    -2,   306,   326,   197,  -166,  -166,
      67,    67,   183,   183,   216,    33,   -26,  -166,  -166,   183,
     166,  -166,    28,  -166,   105,  -166,  -166,   183,   183,   322,
     320,   332,   177,   367,  -166,   183,  -166,   183,   183,   183,
     183,   184,  -166,   183,   211,   183,   219,   154,   237,   245,
    -166,   324,  -166,   382,  -166,   -26,   391,   -26,    94,   351,
    -166,   399,   391,   288,   403,   291,   403,   348,   354,   330,
     330,   330,  -166,  -166,   413,  -166,  -166,  -166,  -166,  -166,
     415,  -166,  -166,  -166,   416,   403,  -166,   418,  -166,   330,
     330,  -166,   369,   170,   170,   375,   216,   422,   170,   423,
     330,   170,   170,   -45,   424,   374,   377,  -166,    38,    54,
     413,   411,   391,  -166,  -166,  -166,   -42,    26,   187,   378,
     170,   419,   170,  -166,   417,   422,   370,  -166,   181,  -166,
     379,   110,   373,  -166,   386,   330,   434,  -166,   330,   170,
     170,   170,   170,   170,   170,   170,   170,   170,   170,   170,
     170,   170,   170,   170,   388,   170,   343,   436,   383,   445,
    -166,  -166,   170,  -166,  -166,  -166,   401,   451,   330,     3,
    -166,  -166,  -166,   117,  -166,   408,  -166,   409,   308,   446,
    -166,   407,   232,   404,    76,  -166,  -166,  -166,  -166,  -166,
    -166,  -166,  -166,  -166,  -166,  -166,  -166,  -166,  -166,  -166,
      67,  -166,   400,   165,  -166,  -166,   405,   412,   410,   421,
      85,  -166,   196,    -5,  -166,  -166,   414,   427,  -166,   170,
     330,   330,  -166,  -166,   425,   286,    93,  -166,  -166,   428,
     170,   426,   330,   429,  -166,   432,  -166,  -166,  -166,   449,
     210,  -166,  -166,   330,   330,   420,   170,   238,  -166,   422,
    -166,  -166,   252,   309,   430,   435,   431,   131,   439,   433,
     330,   440,  -166,  -166,   316,  -166,   330,   124,   330,   448,
    -166,    43,   442,   151,  -166,  -166,   480,   447,   443,   481,
     216,   444,   450,   216,  -166,   452,  -166
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -166,  -166,   376,   -85,  -166,   -50,  -166,  -166,  -166,   437,
    -166,  -166,  -166,  -166,   453,  -166,  -166,  -166,  -166,  -166,
    -166,  -166,  -166,   339,  -166,  -166,  -166,  -124,  -144,   328,
     107,  -166,   167,   268,    42,   -40,  -165
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -134
static const yytype_int16 yytable[] =
{
      52,   197,   198,    29,    56,    68,    48,     1,   205,   206,
      57,   205,    49,    50,    70,   236,   178,   179,   207,    48,
     194,   234,   108,   109,   110,    49,    50,   202,    61,    88,
     243,    88,    48,    91,    62,   186,   187,    99,    49,    50,
      88,    88,    88,    88,   104,    93,   201,   153,   241,    88,
      82,   237,    88,    58,    88,    69,    61,    88,    88,    30,
     305,    83,    62,    89,    71,    88,     4,    88,    88,    88,
      88,    48,    84,    88,    83,    88,   113,    49,    50,   205,
     105,   252,    63,    92,   254,    84,   158,    83,   277,   235,
     106,   205,   227,    19,   293,    94,   205,   233,    84,   176,
     176,   176,   273,   107,   302,   184,   345,   205,   229,    48,
      78,    87,   313,    87,   280,    49,    50,   230,   306,   176,
     176,    48,   100,   101,    87,    87,   196,    49,    50,   205,
     176,    87,   204,     5,    87,    48,    87,    84,   205,    87,
      87,    49,    50,   109,   110,   309,   205,    87,   296,    87,
      87,    87,    87,   115,   327,    87,   315,    87,   248,    32,
     137,   138,    33,   205,    83,   176,   310,   311,   176,   281,
     250,    23,   325,   161,    48,    84,   189,   205,   317,    20,
      49,    50,    72,   333,   342,    48,   176,    48,    73,   322,
     323,    49,    50,    49,    50,   139,   140,   141,   176,   236,
      22,    48,    35,   282,   205,    24,   337,    49,    50,   165,
     166,   347,   341,   105,   343,    36,   142,   143,   205,   144,
      48,   167,   297,   112,   105,   168,    49,    50,   245,   170,
      88,   105,   176,   246,   123,   237,   107,    38,    90,    40,
     190,   131,    83,   238,   303,    98,   247,   107,   304,   102,
     176,   176,    43,    84,   107,    44,   111,    46,   105,   114,
      47,   116,   176,   205,   118,   119,   105,   321,   134,     6,
     192,   192,    54,   176,   176,   199,   136,    45,   192,   203,
     133,   107,   135,    53,   105,   205,   291,   334,    55,   107,
     176,   205,   105,     7,   146,   326,   176,   203,   176,   192,
       8,     9,   147,    66,    10,   205,    67,   107,    11,   328,
     352,    74,   294,   355,    75,   107,   255,   256,   257,   258,
     259,   260,   261,   262,   263,   264,   265,   266,   267,   268,
     269,    76,   271,   161,    48,   105,   162,    77,   105,   192,
      49,    50,   188,   249,   163,   154,   161,    48,   157,   162,
     164,   103,    80,    49,    50,   286,   287,   163,   107,    79,
     288,   107,   205,   164,   339,    81,   329,    96,   340,   165,
     166,    41,    42,   125,    97,   127,   128,   129,   130,   120,
     121,   167,   165,   166,   122,   168,   169,   148,   149,   170,
      25,    26,    27,    28,   167,   171,   192,   150,   168,   272,
     172,   110,   170,   161,    48,   152,   295,   192,   171,   155,
      49,    50,   159,   172,   163,   108,   109,   110,   160,   180,
     164,    -9,   183,   192,   185,   188,   195,   124,   197,   200,
     226,   232,   240,  -132,   239,   244,   249,   242,   251,   165,
     166,   208,  -133,   253,   270,   274,   275,   209,   210,   211,
     212,   167,   213,   214,   276,   168,   169,   279,   278,   170,
     284,   285,   289,   290,   320,   171,   307,   292,   298,   300,
     172,   215,   216,   217,   218,   219,   220,   299,   301,   308,
     324,   318,   312,   319,   314,   316,   348,   351,   332,   330,
     221,   222,   223,   224,   225,   331,   335,   336,   346,   338,
     344,   350,   353,   349,     0,    65,     0,   354,   231,   356,
       0,    95
};

static const yytype_int16 yycheck[] =
{
      40,     6,   167,     6,     6,     6,     4,    36,    53,    54,
      12,    53,    10,    11,     6,    12,   140,   141,    63,     4,
     164,    63,    48,    49,    50,    10,    11,   171,     6,    69,
     195,    71,     4,     6,    12,   159,   160,    77,    10,    11,
      80,    81,    82,    83,    84,     6,   170,   132,   192,    89,
      48,    48,    92,    55,    94,    56,     6,    97,    98,    62,
      65,    59,    12,    48,    56,   105,    61,   107,   108,   109,
     110,     4,    70,   113,    59,   115,    48,    10,    11,    53,
      47,   205,    60,    56,   208,    70,   136,    59,   232,    63,
      57,    53,    54,    59,    18,    56,    53,   182,    70,   139,
     140,   141,   226,    70,    19,   155,    63,    53,    54,     4,
      60,    69,    19,    71,   238,    10,    11,    63,   283,   159,
     160,     4,    80,    81,    82,    83,   166,    10,    11,    53,
     170,    89,   172,     0,    92,     4,    94,    70,    53,    97,
      98,    10,    11,    49,    50,   289,    53,   105,   272,   107,
     108,   109,   110,    48,   319,   113,   300,   115,   198,     6,
       6,     7,     9,    53,    59,   205,   290,   291,   208,    52,
      60,    46,   316,     3,     4,    70,     6,    53,   302,     6,
      10,    11,     6,    52,    60,     4,   226,     4,    12,   313,
     314,    10,    11,    10,    11,    41,    42,    43,   238,    12,
       6,     4,    63,   243,    53,     6,   330,    10,    11,    39,
      40,    60,   336,    47,   338,     6,    62,    63,    53,    65,
       4,    51,    57,    57,    47,    55,    10,    11,    47,    59,
     270,    47,   272,    52,    57,    48,    70,    48,    71,    59,
      70,    57,    59,    56,    48,    48,    65,    70,    52,    82,
     290,   291,    60,    70,    70,    34,    89,     6,    47,    92,
      59,    94,   302,    53,    97,    98,    47,    57,    57,     6,
     163,   164,     6,   313,   314,   168,    57,    63,   171,   172,
     113,    70,   115,    63,    47,    53,    54,   327,    44,    70,
     330,    53,    47,    30,    57,    57,   336,   190,   338,   192,
      37,    38,    57,    31,    41,    53,     6,    70,    45,    57,
     350,    58,   270,   353,    60,    70,   209,   210,   211,   212,
     213,   214,   215,   216,   217,   218,   219,   220,   221,   222,
     223,    56,   225,     3,     4,    47,     6,    56,    47,   232,
      10,    11,    56,    57,    14,    57,     3,     4,    57,     6,
      20,    83,    59,    10,    11,    47,    48,    14,    70,     9,
      52,    70,    53,    20,    48,    51,    57,    61,    52,    39,
      40,    32,    33,   105,    48,   107,   108,   109,   110,    57,
      60,    51,    39,    40,    52,    55,    56,    63,     6,    59,
      14,    15,    16,    17,    51,    65,   289,     6,    55,    56,
      70,    50,    59,     3,     4,     6,     6,   300,    65,     6,
      10,    11,    64,    70,    14,    48,    49,    50,    64,     6,
      20,     6,     6,   316,     6,    56,    51,    60,     6,     6,
      56,    20,    13,    56,    56,    65,    57,    20,    65,    39,
      40,    17,    56,     9,    56,     9,    63,    23,    24,    25,
      26,    51,    28,    29,     9,    55,    56,     6,    57,    59,
      52,    52,    16,    56,    15,    65,    52,    63,    63,    59,
      70,    47,    48,    49,    50,    51,    52,    65,    57,    52,
      60,    52,    57,    51,    56,    59,     6,     6,    57,    59,
      66,    67,    68,    69,    70,    60,    57,    64,    56,    59,
      52,    58,    58,    56,    -1,    52,    -1,    57,   180,    57,
      -1,    74
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,    36,    72,    88,    61,     0,     6,    30,    37,    38,
      41,    45,    73,    81,    82,    89,    90,    92,    87,    59,
       6,    93,     6,    46,     6,    73,    73,    73,    73,     6,
      62,    86,     6,     9,    94,    63,     6,    91,    48,    83,
      59,    94,    94,    60,    34,    63,     6,    59,     4,    10,
      11,    85,   106,    63,     6,    44,     6,    12,    55,    77,
      80,     6,    12,    60,    84,    85,    31,     6,     6,    56,
       6,    56,     6,    12,    58,    60,    56,    56,    60,     9,
      59,    51,    48,    59,    70,   103,   104,   105,   106,    48,
     103,     6,    56,     6,    56,    80,    61,    48,    48,   106,
     105,   105,   103,   104,   106,    47,    57,    70,    48,    49,
      50,   103,    57,    48,   103,    48,   103,    95,   103,   103,
      57,    60,    52,    57,    60,   104,    79,   104,   104,   104,
     104,    57,    78,   103,    57,   103,    57,     6,     7,    41,
      42,    43,    62,    63,    65,    96,    57,    57,    63,     6,
       6,    74,     6,    74,    57,     6,    76,    57,    76,    64,
      64,     3,     6,    14,    20,    39,    40,    51,    55,    56,
      59,    65,    70,    98,   101,   105,   106,   107,    98,    98,
       6,   100,    75,     6,    76,     6,    98,    98,    56,     6,
      70,    99,   101,   106,    99,    51,   106,     6,   107,   101,
       6,    98,    99,   101,   106,    53,    54,    63,    17,    23,
      24,    25,    26,    28,    29,    47,    48,    49,    50,    51,
      52,    66,    67,    68,    69,    70,    56,    54,    97,    54,
      63,   100,    20,    74,    63,    63,    12,    48,    56,    56,
      13,    99,    20,   107,    65,    47,    52,    65,   106,    57,
      60,    65,    98,     9,    98,   101,   101,   101,   101,   101,
     101,   101,   101,   101,   101,   101,   101,   101,   101,   101,
      56,   101,    56,    98,     9,    63,     9,    99,    57,     6,
      98,    52,   106,   102,    52,    52,    47,    48,    52,    16,
      56,    54,    63,    18,   105,     6,    98,    57,    63,    65,
      59,    57,    19,    48,    52,    65,   107,    52,    52,    99,
      98,    98,    57,    19,    56,    99,    59,    98,    52,    51,
      15,    57,    98,    98,    60,    99,    57,   107,    57,    57,
      59,    60,    57,    52,   106,    57,    64,    98,    59,    48,
      52,    98,    60,    98,    52,    63,    56,    60,     6,    56,
      58,     6,   106,    58,    57,   106,    57
};

#define yyerrok		(yyerrstatus = 0)
#define yyclearin	(yychar = YYEMPTY)
#define YYEMPTY		(-2)
#define YYEOF		0

#define YYACCEPT	goto yyacceptlab
#define YYABORT		goto yyabortlab
#define YYERROR		goto yyerrorlab


/* Like YYERROR except do call yyerror.  This remains here temporarily
   to ease the transition to the new meaning of YYERROR, for GCC.
   Once GCC version 2 has supplanted version 1, this can go.  */

#define YYFAIL		goto yyerrlab

#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)					\
do								\
  if (yychar == YYEMPTY && yylen == 1)				\
    {								\
      yychar = (Token);						\
      yylval = (Value);						\
      yytoken = YYTRANSLATE (yychar);				\
      YYPOPSTACK (1);						\
      goto yybackup;						\
    }								\
  else								\
    {								\
      yyerror (yyscanner, YY_("syntax error: cannot back up")); \
      YYERROR;							\
    }								\
while (YYID (0))


#define YYTERROR	1
#define YYERRCODE	256


/* YYLLOC_DEFAULT -- Set CURRENT to span from RHS[1] to RHS[N].
   If N is 0, then set CURRENT to the empty location which ends
   the previous symbol: RHS[0] (always defined).  */

#define YYRHSLOC(Rhs, K) ((Rhs)[K])
#ifndef YYLLOC_DEFAULT
# define YYLLOC_DEFAULT(Current, Rhs, N)				\
    do									\
      if (YYID (N))                                                    \
	{								\
	  (Current).first_line   = YYRHSLOC (Rhs, 1).first_line;	\
	  (Current).first_column = YYRHSLOC (Rhs, 1).first_column;	\
	  (Current).last_line    = YYRHSLOC (Rhs, N).last_line;		\
	  (Current).last_column  = YYRHSLOC (Rhs, N).last_column;	\
	}								\
      else								\
	{								\
	  (Current).first_line   = (Current).last_line   =		\
	    YYRHSLOC (Rhs, 0).last_line;				\
	  (Current).first_column = (Current).last_column =		\
	    YYRHSLOC (Rhs, 0).last_column;				\
	}								\
    while (YYID (0))
#endif


/* YY_LOCATION_PRINT -- Print the location on the stream.
   This macro was not mandated originally: define only if we know
   we won't break user code: when these are the locations we know.  */

#ifndef YY_LOCATION_PRINT
# if defined YYLTYPE_IS_TRIVIAL && YYLTYPE_IS_TRIVIAL
#  define YY_LOCATION_PRINT(File, Loc)			\
     fprintf (File, "%d.%d-%d.%d",			\
	      (Loc).first_line, (Loc).first_column,	\
	      (Loc).last_line,  (Loc).last_column)
# else
#  define YY_LOCATION_PRINT(File, Loc) ((void) 0)
# endif
#endif


/* YYLEX -- calling `yylex' with the right arguments.  */

#ifdef YYLEX_PARAM
# define YYLEX yylex (&yylval, YYLEX_PARAM)
#else
# define YYLEX yylex (&yylval, yyscanner)
#endif

/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)			\
do {						\
  if (yydebug)					\
    YYFPRINTF Args;				\
} while (YYID (0))

# define YY_SYMBOL_PRINT(Title, Type, Value, Location)			  \
do {									  \
  if (yydebug)								  \
    {									  \
      YYFPRINTF (stderr, "%s ", Title);					  \
      yy_symbol_print (stderr,						  \
		  Type, Value, yyscanner); \
      YYFPRINTF (stderr, "\n");						  \
    }									  \
} while (YYID (0))


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep, yyscan_t yyscanner)
#else
static void
yy_symbol_value_print (yyoutput, yytype, yyvaluep, yyscanner)
    FILE *yyoutput;
    int yytype;
    YYSTYPE const * const yyvaluep;
    yyscan_t yyscanner;
#endif
{
  if (!yyvaluep)
    return;
  YYUSE (yyscanner);
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# else
  YYUSE (yyoutput);
# endif
  switch (yytype)
    {
      default:
	break;
    }
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep, yyscan_t yyscanner)
#else
static void
yy_symbol_print (yyoutput, yytype, yyvaluep, yyscanner)
    FILE *yyoutput;
    int yytype;
    YYSTYPE const * const yyvaluep;
    yyscan_t yyscanner;
#endif
{
  if (yytype < YYNTOKENS)
    YYFPRINTF (yyoutput, "token %s (", yytname[yytype]);
  else
    YYFPRINTF (yyoutput, "nterm %s (", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep, yyscanner);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_stack_print (yytype_int16 *bottom, yytype_int16 *top)
#else
static void
yy_stack_print (bottom, top)
    yytype_int16 *bottom;
    yytype_int16 *top;
#endif
{
  YYFPRINTF (stderr, "Stack now");
  for (; bottom <= top; ++bottom)
    YYFPRINTF (stderr, " %d", *bottom);
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)				\
do {								\
  if (yydebug)							\
    yy_stack_print ((Bottom), (Top));				\
} while (YYID (0))


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_reduce_print (YYSTYPE *yyvsp, int yyrule, yyscan_t yyscanner)
#else
static void
yy_reduce_print (yyvsp, yyrule, yyscanner)
    YYSTYPE *yyvsp;
    int yyrule;
    yyscan_t yyscanner;
#endif
{
  int yynrhs = yyr2[yyrule];
  int yyi;
  unsigned long int yylno = yyrline[yyrule];
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
	     yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      fprintf (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr, yyrhs[yyprhs[yyrule] + yyi],
		       &(yyvsp[(yyi + 1) - (yynrhs)])
		       		       , yyscanner);
      fprintf (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)		\
do {					\
  if (yydebug)				\
    yy_reduce_print (yyvsp, Rule, yyscanner); \
} while (YYID (0))

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef	YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif



#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static YYSIZE_T
yystrlen (const char *yystr)
#else
static YYSIZE_T
yystrlen (yystr)
    const char *yystr;
#endif
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static char *
yystpcpy (char *yydest, const char *yysrc)
#else
static char *
yystpcpy (yydest, yysrc)
    char *yydest;
    const char *yysrc;
#endif
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
	switch (*++yyp)
	  {
	  case '\'':
	  case ',':
	    goto do_not_strip_quotes;

	  case '\\':
	    if (*++yyp != '\\')
	      goto do_not_strip_quotes;
	    /* Fall through.  */
	  default:
	    if (yyres)
	      yyres[yyn] = *yyp;
	    yyn++;
	    break;

	  case '"':
	    if (yyres)
	      yyres[yyn] = '\0';
	    return yyn;
	  }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into YYRESULT an error message about the unexpected token
   YYCHAR while in state YYSTATE.  Return the number of bytes copied,
   including the terminating null byte.  If YYRESULT is null, do not
   copy anything; just return the number of bytes that would be
   copied.  As a special case, return 0 if an ordinary "syntax error"
   message will do.  Return YYSIZE_MAXIMUM if overflow occurs during
   size calculation.  */
static YYSIZE_T
yysyntax_error (char *yyresult, int yystate, int yychar)
{
  int yyn = yypact[yystate];

  if (! (YYPACT_NINF < yyn && yyn <= YYLAST))
    return 0;
  else
    {
      int yytype = YYTRANSLATE (yychar);
      YYSIZE_T yysize0 = yytnamerr (0, yytname[yytype]);
      YYSIZE_T yysize = yysize0;
      YYSIZE_T yysize1;
      int yysize_overflow = 0;
      enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
      char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
      int yyx;

# if 0
      /* This is so xgettext sees the translatable formats that are
	 constructed on the fly.  */
      YY_("syntax error, unexpected %s");
      YY_("syntax error, unexpected %s, expecting %s");
      YY_("syntax error, unexpected %s, expecting %s or %s");
      YY_("syntax error, unexpected %s, expecting %s or %s or %s");
      YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s");
# endif
      char *yyfmt;
      char const *yyf;
      static char const yyunexpected[] = "syntax error, unexpected %s";
      static char const yyexpecting[] = ", expecting %s";
      static char const yyor[] = " or %s";
      char yyformat[sizeof yyunexpected
		    + sizeof yyexpecting - 1
		    + ((YYERROR_VERBOSE_ARGS_MAXIMUM - 2)
		       * (sizeof yyor - 1))];
      char const *yyprefix = yyexpecting;

      /* Start YYX at -YYN if negative to avoid negative indexes in
	 YYCHECK.  */
      int yyxbegin = yyn < 0 ? -yyn : 0;

      /* Stay within bounds of both yycheck and yytname.  */
      int yychecklim = YYLAST - yyn + 1;
      int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
      int yycount = 1;

      yyarg[0] = yytname[yytype];
      yyfmt = yystpcpy (yyformat, yyunexpected);

      for (yyx = yyxbegin; yyx < yyxend; ++yyx)
	if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR)
	  {
	    if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
	      {
		yycount = 1;
		yysize = yysize0;
		yyformat[sizeof yyunexpected - 1] = '\0';
		break;
	      }
	    yyarg[yycount++] = yytname[yyx];
	    yysize1 = yysize + yytnamerr (0, yytname[yyx]);
	    yysize_overflow |= (yysize1 < yysize);
	    yysize = yysize1;
	    yyfmt = yystpcpy (yyfmt, yyprefix);
	    yyprefix = yyor;
	  }

      yyf = YY_(yyformat);
      yysize1 = yysize + yystrlen (yyf);
      yysize_overflow |= (yysize1 < yysize);
      yysize = yysize1;

      if (yysize_overflow)
	return YYSIZE_MAXIMUM;

      if (yyresult)
	{
	  /* Avoid sprintf, as that infringes on the user's name space.
	     Don't have undefined behavior even if the translation
	     produced a string with the wrong number of "%s"s.  */
	  char *yyp = yyresult;
	  int yyi = 0;
	  while ((*yyp = *yyf) != '\0')
	    {
	      if (*yyp == '%' && yyf[1] == 's' && yyi < yycount)
		{
		  yyp += yytnamerr (yyp, yyarg[yyi++]);
		  yyf += 2;
		}
	      else
		{
		  yyp++;
		  yyf++;
		}
	    }
	}
      return yysize;
    }
}
#endif /* YYERROR_VERBOSE */


/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep, yyscan_t yyscanner)
#else
static void
yydestruct (yymsg, yytype, yyvaluep, yyscanner)
    const char *yymsg;
    int yytype;
    YYSTYPE *yyvaluep;
    yyscan_t yyscanner;
#endif
{
  YYUSE (yyvaluep);
  YYUSE (yyscanner);

  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  switch (yytype)
    {

      default:
	break;
    }
}


/* Prevent warnings from -Wmissing-prototypes.  */

#ifdef YYPARSE_PARAM
#if defined __STDC__ || defined __cplusplus
int yyparse (void *YYPARSE_PARAM);
#else
int yyparse ();
#endif
#else /* ! YYPARSE_PARAM */
#if defined __STDC__ || defined __cplusplus
int yyparse (yyscan_t yyscanner);
#else
int yyparse ();
#endif
#endif /* ! YYPARSE_PARAM */






/*----------.
| yyparse.  |
`----------*/

#ifdef YYPARSE_PARAM
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yyparse (void *YYPARSE_PARAM)
#else
int
yyparse (YYPARSE_PARAM)
    void *YYPARSE_PARAM;
#endif
#else /* ! YYPARSE_PARAM */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yyparse (yyscan_t yyscanner)
#else
int
yyparse (yyscanner)
    yyscan_t yyscanner;
#endif
#endif
{
  /* The look-ahead symbol.  */
int yychar;

/* The semantic value of the look-ahead symbol.  */
YYSTYPE yylval;

/* Number of syntax errors so far.  */
int yynerrs;

  int yystate;
  int yyn;
  int yyresult;
  /* Number of tokens to shift before error messages enabled.  */
  int yyerrstatus;
  /* Look-ahead token as an internal (translated) token number.  */
  int yytoken = 0;
#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

  /* Three stacks and their tools:
     `yyss': related to states,
     `yyvs': related to semantic values,
     `yyls': related to locations.

     Refer to the stacks thru separate pointers, to allow yyoverflow
     to reallocate them elsewhere.  */

  /* The state stack.  */
  yytype_int16 yyssa[YYINITDEPTH];
  yytype_int16 *yyss = yyssa;
  yytype_int16 *yyssp;

  /* The semantic value stack.  */
  YYSTYPE yyvsa[YYINITDEPTH];
  YYSTYPE *yyvs = yyvsa;
  YYSTYPE *yyvsp;



#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  YYSIZE_T yystacksize = YYINITDEPTH;

  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;


  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY;		/* Cause a token to be read.  */

  /* Initialize stack pointers.
     Waste one element of value and location stack
     so that they stay on the same level as the state stack.
     The wasted elements are never initialized.  */

  yyssp = yyss;
  yyvsp = yyvs;

  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
	/* Give user a chance to reallocate the stack.  Use copies of
	   these so that the &'s don't force the real ones into
	   memory.  */
	YYSTYPE *yyvs1 = yyvs;
	yytype_int16 *yyss1 = yyss;


	/* Each stack pointer address is followed by the size of the
	   data in use in that stack, in bytes.  This used to be a
	   conditional around just the two extra args, but that might
	   be undefined if yyoverflow is a macro.  */
	yyoverflow (YY_("memory exhausted"),
		    &yyss1, yysize * sizeof (*yyssp),
		    &yyvs1, yysize * sizeof (*yyvsp),

		    &yystacksize);

	yyss = yyss1;
	yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
	goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
	yystacksize = YYMAXDEPTH;

      {
	yytype_int16 *yyss1 = yyss;
	union yyalloc *yyptr =
	  (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
	if (! yyptr)
	  goto yyexhaustedlab;
	YYSTACK_RELOCATE (yyss);
	YYSTACK_RELOCATE (yyvs);

#  undef YYSTACK_RELOCATE
	if (yyss1 != yyssa)
	  YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;


      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
		  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
	YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     look-ahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to look-ahead token.  */
  yyn = yypact[yystate];
  if (yyn == YYPACT_NINF)
    goto yydefault;

  /* Not known => get a look-ahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid look-ahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = YYLEX;
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yyn == 0 || yyn == YYTABLE_NINF)
	goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  if (yyn == YYFINAL)
    YYACCEPT;

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the look-ahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token unless it is eof.  */
  if (yychar != YYEOF)
    yychar = YYEMPTY;

  yystate = yyn;
  *++yyvsp = yylval;

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     `$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
        case 2:
#line 129 "InputParser/InputParser.yy"
    { solution.start(); int tmp= envt->doallpairs() ; solution.stop(); return tmp; }
    break;

  case 3:
#line 132 "InputParser/InputParser.yy"
    {}
    break;

  case 4:
#line 133 "InputParser/InputParser.yy"
    {}
    break;

  case 5:
#line 134 "InputParser/InputParser.yy"
    {}
    break;

  case 6:
#line 135 "InputParser/InputParser.yy"
    {}
    break;

  case 7:
#line 136 "InputParser/InputParser.yy"
    {}
    break;

  case 8:
#line 139 "InputParser/InputParser.yy"
    { 
    if(Gvartype == TUPLE){
        currentBD->create_inputs( -1, OutType::getTuple(tupleName), *(yyvsp[(1) - (1)].strConst));
    }
    else
    if( Gvartype == INT){
		currentBD->create_inputs( 2 /*NINPUTS*/, OutType::INT , *(yyvsp[(1) - (1)].strConst)); 
	}else{
		if(Gvartype==FLOAT){
			currentBD->create_inputs(2, OutType::FLOAT, *(yyvsp[(1) - (1)].strConst)); 
		}else{
			currentBD->create_inputs(-1, OutType::BOOL, *(yyvsp[(1) - (1)].strConst)); 
		}
	}	

}
    break;

  case 9:
#line 155 "InputParser/InputParser.yy"
    {
	if(Gvartype == TUPLE){
        currentBD->create_inputs( -1, OutType::getTuple(tupleName), *(yyvsp[(1) - (1)].strConst));
    }
    else
    if( Gvartype == INT){
		currentBD->create_inputs( 2 /*NINPUTS*/, OutType::INT , *(yyvsp[(1) - (1)].strConst)); 
	}else{
		if(Gvartype==FLOAT){
			currentBD->create_inputs(2, OutType::FLOAT, *(yyvsp[(1) - (1)].strConst)); 
		}else{
			currentBD->create_inputs(-1, OutType::BOOL, *(yyvsp[(1) - (1)].strConst)); 
		}
	}	
}
    break;

  case 11:
#line 171 "InputParser/InputParser.yy"
    { 	 currentBD->create_outputs(-1, *(yyvsp[(1) - (1)].strConst)); }
    break;

  case 12:
#line 172 "InputParser/InputParser.yy"
    {
	
	currentBD->create_outputs(-1, *(yyvsp[(1) - (2)].strConst));
}
    break;

  case 13:
#line 178 "InputParser/InputParser.yy"
    {  
	if( (yyvsp[(1) - (2)].variableType) == INT){

		currentBD->create_inputs( 2 /*NINPUTS*/, OutType::INT , *(yyvsp[(2) - (2)].strConst)); 
	}else{
		if((yyvsp[(1) - (2)].variableType) == FLOAT){
			currentBD->create_inputs(2, OutType::FLOAT, *(yyvsp[(2) - (2)].strConst)); 
		}else{
			currentBD->create_inputs(-1, OutType::BOOL, *(yyvsp[(2) - (2)].strConst)); 
		}
	}	
	delete (yyvsp[(2) - (2)].strConst);
}
    break;

  case 14:
#line 191 "InputParser/InputParser.yy"
    {

    currentBD->create_inputs( -1 , OutType::getTuple(*(yyvsp[(1) - (2)].strConst)), *(yyvsp[(2) - (2)].strConst));
       

    delete (yyvsp[(2) - (2)].strConst);
}
    break;

  case 15:
#line 198 "InputParser/InputParser.yy"
    {

    currentBD->create_inputs( -1 , OutType::getTuple(*(yyvsp[(1) - (5)].strConst)) , *(yyvsp[(2) - (5)].strConst), -1, (yyvsp[(4) - (5)].intConst));
       

    delete (yyvsp[(2) - (5)].strConst);
}
    break;

  case 16:
#line 205 "InputParser/InputParser.yy"
    {
 	 if( (yyvsp[(2) - (3)].variableType) == INT){

		 currentBD->create_outputs(2 /* NINPUTS */, *(yyvsp[(3) - (3)].strConst));
 	 }else{

	 	 currentBD->create_outputs(-1, *(yyvsp[(3) - (3)].strConst)); 
 	 }
	 delete (yyvsp[(3) - (3)].strConst);
 }
    break;

  case 17:
#line 215 "InputParser/InputParser.yy"
    {

    currentBD->create_outputs(-1, *(yyvsp[(3) - (3)].strConst));
    delete (yyvsp[(3) - (3)].strConst);
 }
    break;

  case 18:
#line 221 "InputParser/InputParser.yy"
    {  
	if( (yyvsp[(1) - (6)].variableType) == INT){

		currentBD->create_inputs( 2 /*NINPUTS*/, OutType::INT_ARR , *(yyvsp[(6) - (6)].strConst), (yyvsp[(4) - (6)].intConst)); 
	}else{
		if((yyvsp[(1) - (6)].variableType) == FLOAT){
			currentBD->create_inputs(2, OutType::FLOAT_ARR, *(yyvsp[(6) - (6)].strConst), (yyvsp[(4) - (6)].intConst)); 
		}else{
			currentBD->create_inputs(-1, OutType::BOOL_ARR, *(yyvsp[(6) - (6)].strConst), (yyvsp[(4) - (6)].intConst)); 
		}
	}	
	delete (yyvsp[(6) - (6)].strConst);
}
    break;

  case 19:
#line 235 "InputParser/InputParser.yy"
    {
    currentBD->create_inputs(-1, OutType::getTuple(*(yyvsp[(1) - (6)].strConst)), *(yyvsp[(6) - (6)].strConst), (yyvsp[(4) - (6)].intConst));
}
    break;

  case 20:
#line 239 "InputParser/InputParser.yy"
    {
 	 if( (yyvsp[(2) - (7)].variableType) == INT){
		 currentBD->create_outputs(2 /* NINPUTS */, *(yyvsp[(7) - (7)].strConst));
 	 }else{

	 	 currentBD->create_outputs(-1, *(yyvsp[(7) - (7)].strConst)); 
 	 }
	 delete (yyvsp[(7) - (7)].strConst);
 }
    break;

  case 21:
#line 248 "InputParser/InputParser.yy"
    {
  currentBD->create_outputs(-1,*(yyvsp[(7) - (7)].strConst));
 }
    break;

  case 22:
#line 251 "InputParser/InputParser.yy"
    {Gvartype = (yyvsp[(1) - (4)].variableType); }
    break;

  case 24:
#line 252 "InputParser/InputParser.yy"
    {Gvartype = TUPLE; tupleName = *(yyvsp[(1) - (4)].strConst);}
    break;

  case 31:
#line 261 "InputParser/InputParser.yy"
    {isModel=true; }
    break;

  case 32:
#line 261 "InputParser/InputParser.yy"
    {isModel=false; }
    break;

  case 33:
#line 264 "InputParser/InputParser.yy"
    {		modelBuilding.restart ();
		if(currentBD!= NULL){
			delete currentBD;
		}

		currentBD = envt->newFunction(*(yyvsp[(2) - (2)].strConst), isModel);

		delete (yyvsp[(2) - (2)].strConst);

}
    break;

  case 34:
#line 274 "InputParser/InputParser.yy"
    { 
	currentBD->finalize();
	modelBuilding.stop();
}
    break;

  case 35:
#line 280 "InputParser/InputParser.yy"
    {
    if( (yyvsp[(1) - (1)].variableType) == INT){ (yyval.otype) = OutType::INT;}
    if( (yyvsp[(1) - (1)].variableType) == BIT){ (yyval.otype) = OutType::BOOL;}
	if( (yyvsp[(1) - (1)].variableType) == FLOAT){ (yyval.otype) = OutType::FLOAT;}
    if( (yyvsp[(1) - (1)].variableType) == INT_ARR){ (yyval.otype) = OutType::INT_ARR;}
    if( (yyvsp[(1) - (1)].variableType) == BIT_ARR){ (yyval.otype) = OutType::BOOL_ARR;}
    if( (yyvsp[(1) - (1)].variableType) == FLOAT_ARR){ (yyval.otype) = OutType::FLOAT_ARR;}
}
    break;

  case 36:
#line 288 "InputParser/InputParser.yy"
    {
    if ((yyvsp[(1) - (5)].variableType) == INT) {(yyval.otype) = OutType::INT_ARR;}
    if( (yyvsp[(1) - (5)].variableType) == BIT){ (yyval.otype) = OutType::BOOL_ARR;}
    if( (yyvsp[(1) - (5)].variableType) == FLOAT){ (yyval.otype) = OutType::FLOAT_ARR;}
}
    break;

  case 37:
#line 293 "InputParser/InputParser.yy"
    {
  (yyval.otype) = ((Tuple*)OutType::getTuple(*(yyvsp[(1) - (5)].strConst)))->arr;
}
    break;

  case 38:
#line 296 "InputParser/InputParser.yy"
    { 
    (yyval.otype) = OutType::getTuple(*(yyvsp[(1) - (1)].strConst));
}
    break;

  case 39:
#line 300 "InputParser/InputParser.yy"
    {/* Empty */  (yyval.tVector) = new vector<OutType*>(); }
    break;

  case 40:
#line 301 "InputParser/InputParser.yy"
    {
    (yyvsp[(1) - (2)].tVector)->push_back( (yyvsp[(2) - (2)].otype) );
    (yyval.tVector) = (yyvsp[(1) - (2)].tVector);
}
    break;

  case 41:
#line 305 "InputParser/InputParser.yy"
    {
    OutType* type;
    if ((yyvsp[(2) - (5)].variableType) == INT) {type = OutType::INT_ARR;}
    if( (yyvsp[(2) - (5)].variableType) == BIT){ type = OutType::BOOL_ARR;}
    if( (yyvsp[(2) - (5)].variableType) == FLOAT){type = OutType::FLOAT_ARR;}
    for (int i = 0; i < (yyvsp[(4) - (5)].intConst); i++ ) {
        (yyvsp[(1) - (5)].tVector)->push_back (type );
    }
    (yyval.tVector) = (yyvsp[(1) - (5)].tVector);

}
    break;

  case 42:
#line 317 "InputParser/InputParser.yy"
    {
//add type
    OutType::makeTuple(*(yyvsp[(1) - (4)].strConst), *(yyvsp[(3) - (4)].tVector), -1);

}
    break;

  case 43:
#line 322 "InputParser/InputParser.yy"
    {
    OutType::makeTuple(*(yyvsp[(1) - (5)].strConst), *(yyvsp[(4) - (5)].tVector), (yyvsp[(3) - (5)].intConst));
}
    break;

  case 44:
#line 326 "InputParser/InputParser.yy"
    { /* Empty */ }
    break;

  case 45:
#line 327 "InputParser/InputParser.yy"
    { }
    break;

  case 46:
#line 329 "InputParser/InputParser.yy"
    {/* Empty */}
    break;

  case 47:
#line 330 "InputParser/InputParser.yy"
    { }
    break;

  case 48:
#line 332 "InputParser/InputParser.yy"
    {
  envt->registerFunctionReplace(*(yyvsp[(4) - (10)].strConst), *(yyvsp[(2) - (10)].strConst), *(yyvsp[(6) - (10)].strConst), (yyvsp[(8) - (10)].intConst));
}
    break;

  case 49:
#line 338 "InputParser/InputParser.yy"
    {
	envt->fixes(*(yyvsp[(2) - (3)].strConst));
}
    break;

  case 50:
#line 343 "InputParser/InputParser.yy"
    {
	if(PARAMS->interactive){
		(yyval.bdag) = envt->prepareMiter(envt->getCopy(*(yyvsp[(3) - (3)].strConst)),  envt->getCopy(*(yyvsp[(1) - (3)].strConst)), envt->inlineAmnt());
	}else{
		envt->addspskpair(*(yyvsp[(3) - (3)].strConst), *(yyvsp[(1) - (3)].strConst));
	}		
}
    break;

  case 51:
#line 350 "InputParser/InputParser.yy"
    {
	
	if(PARAMS->interactive){
		(yyval.bdag) = envt->prepareMiter(envt->getCopy(*(yyvsp[(3) - (5)].strConst)),  envt->getCopy(*(yyvsp[(1) - (5)].strConst)), envt->inlineAmnt());
	}else{
		envt->addspskpair(*(yyvsp[(3) - (5)].strConst), *(yyvsp[(1) - (5)].strConst), *(yyvsp[(5) - (5)].strConst));
		delete (yyvsp[(5) - (5)].strConst);
	}
}
    break;

  case 52:
#line 362 "InputParser/InputParser.yy"
    {if(PARAMS->interactive){ solution.restart();} }
    break;

  case 53:
#line 363 "InputParser/InputParser.yy"
    {
	if(PARAMS->interactive){
		int tt = envt->assertDAG((yyvsp[(3) - (4)].bdag), std::cout, "");
		envt->printControls("");
		solution.stop();
		cout<<"COMPLETED"<<endl;
		if(tt != 0){
			return tt;
		}
	}
}
    break;

  case 54:
#line 375 "InputParser/InputParser.yy"
    {
	int tt = envt->runCommand(*(yyvsp[(1) - (5)].strConst), *(yyvsp[(3) - (5)].sList));
	delete (yyvsp[(1) - (5)].strConst);
	delete (yyvsp[(3) - (5)].sList);
	if(tt >= 0){
		return tt;
	}
}
    break;

  case 55:
#line 384 "InputParser/InputParser.yy"
    {
	(yyval.sList) = new list<string*>();	
}
    break;

  case 56:
#line 387 "InputParser/InputParser.yy"
    {
	(yyval.sList) = (yyvsp[(2) - (2)].sList);
	(yyval.sList)->push_back( (yyvsp[(1) - (2)].strConst));
}
    break;

  case 57:
#line 391 "InputParser/InputParser.yy"
    {
	(yyval.sList) = (yyvsp[(2) - (2)].sList);
	(yyval.sList)->push_back( (yyvsp[(1) - (2)].strConst));
}
    break;

  case 58:
#line 397 "InputParser/InputParser.yy"
    { /* Empty */ }
    break;

  case 59:
#line 398 "InputParser/InputParser.yy"
    { /* */ }
    break;

  case 60:
#line 401 "InputParser/InputParser.yy"
    {  (yyval.intConst)=0;  /* */ }
    break;

  case 61:
#line 402 "InputParser/InputParser.yy"
    {
	currentBD->alias( *(yyvsp[(1) - (4)].strConst), (yyvsp[(3) - (4)].bnode));
	delete (yyvsp[(1) - (4)].strConst);
}
    break;

  case 62:
#line 406 "InputParser/InputParser.yy"
    {

	list<string*>* childs = (yyvsp[(2) - (11)].sList);
	list<string*>::reverse_iterator it = childs->rbegin();
	
	list<bool_node*>* oldchilds = (yyvsp[(4) - (11)].nList);
	list<bool_node*>::reverse_iterator oldit = oldchilds->rbegin();
	
	bool_node* rhs;
	rhs = (yyvsp[(10) - (11)].bnode);
	int bigN = childs->size();
	Assert( bigN == oldchilds->size(), "This can't happen");	

	for(int i=0; i<bigN; ++i, ++it, ++oldit){		
		ARRASS_node* an = dynamic_cast<ARRASS_node*>(newNode(bool_node::ARRASS, 2));
		an->set_parent(1, *oldit);			
		an->set_parent(2, rhs);
		Assert( rhs != NULL, "AAARRRGH This shouldn't happen !!");
		Assert((yyvsp[(7) - (11)].bnode) != NULL, "1: THIS CAN'T HAPPEN!!");
		an->quant = i;		
		currentBD->alias( *(*it), currentBD->new_node((yyvsp[(7) - (11)].bnode),  NULL,  an) );
		delete *it;
	}
	delete childs;
	delete oldchilds;	
}
    break;

  case 63:
#line 433 "InputParser/InputParser.yy"
    {
	Assert(false, "UNREACHABLE");
	currentBD->create_outputs(2 /*NINPUTS*/, (yyvsp[(3) - (4)].bnode), *(yyvsp[(1) - (4)].strConst));
	delete (yyvsp[(1) - (4)].strConst);
}
    break;

  case 64:
#line 438 "InputParser/InputParser.yy"
    {
  if ((yyvsp[(2) - (3)].bnode)) {
    /* Asserting an expression, construct assert node. */
    
    currentBD->new_node ((yyvsp[(2) - (3)].bnode), NULL, bool_node::ASSERT);
  }
}
    break;

  case 65:
#line 445 "InputParser/InputParser.yy"
    {
  if ((yyvsp[(2) - (5)].bnode)) {
    /* Asserting an expression, construct assert node. */
	if(!((yyvsp[(2) - (5)].bnode)->type == bool_node::CONST && dynamic_cast<CONST_node*>((yyvsp[(2) - (5)].bnode))->getVal() == 1)){
		ASSERT_node* bn = dynamic_cast<ASSERT_node*>(newNode(bool_node::ASSERT));
		bn->setMsg(*(yyvsp[(4) - (5)].strConst));
		currentBD->new_node ((yyvsp[(2) - (5)].bnode), NULL, bn);
	}    
    delete (yyvsp[(4) - (5)].strConst);
  }
}
    break;

  case 66:
#line 456 "InputParser/InputParser.yy"
    {
  if ((yyvsp[(2) - (3)].bnode)) {
    /* Asserting an expression, construct assert node. */
    
    ASSERT_node* bn = dynamic_cast<ASSERT_node*>(newNode(bool_node::ASSERT));
    bn->makeHardAssert();
    currentBD->new_node((yyvsp[(2) - (3)].bnode), NULL, bn);
  }
}
    break;

  case 67:
#line 465 "InputParser/InputParser.yy"
    {
  if ((yyvsp[(2) - (5)].bnode)) {
    /* Asserting an expression, construct assert node. */
	if(!((yyvsp[(2) - (5)].bnode)->type == bool_node::CONST && dynamic_cast<CONST_node*>((yyvsp[(2) - (5)].bnode))->getVal() == 1)){
		ASSERT_node* bn = dynamic_cast<ASSERT_node*>(newNode(bool_node::ASSERT));
		bn->setMsg(*(yyvsp[(4) - (5)].strConst));
    bn->makeHardAssert();
		currentBD->new_node ((yyvsp[(2) - (5)].bnode), NULL, bn);
	}    
    delete (yyvsp[(4) - (5)].strConst);
  }
}
    break;

  case 68:
#line 478 "InputParser/InputParser.yy"
    {
  if ((yyvsp[(2) - (4)].bnode)) {
    /* Asserting an expression, construct assert node. */
	if(!((yyvsp[(2) - (4)].bnode)->type == bool_node::CONST && dynamic_cast<CONST_node*>((yyvsp[(2) - (4)].bnode))->getVal() == 1)){
		ASSERT_node* bn = dynamic_cast<ASSERT_node*>(newNode(bool_node::ASSERT));
		bn->makeAssume();
		if ((yyvsp[(3) - (4)].strConst)) {
			bn->setMsg(*(yyvsp[(3) - (4)].strConst));
		}
		currentBD->new_node ((yyvsp[(2) - (4)].bnode), NULL, bn);
	}
	if ((yyvsp[(3) - (4)].strConst)) {
		delete (yyvsp[(3) - (4)].strConst);
	}
  }
}
    break;

  case 69:
#line 495 "InputParser/InputParser.yy"
    { (yyval.strConst) = (yyvsp[(2) - (2)].strConst); }
    break;

  case 70:
#line 496 "InputParser/InputParser.yy"
    { (yyval.strConst) = 0; }
    break;

  case 71:
#line 498 "InputParser/InputParser.yy"
    { (yyval.bnode) = (yyvsp[(1) - (1)].bnode); }
    break;

  case 72:
#line 499 "InputParser/InputParser.yy"
    {
	(yyval.bnode) = currentBD->new_node((yyvsp[(1) - (3)].bnode),  (yyvsp[(3) - (3)].bnode), bool_node::AND);	
}
    break;

  case 73:
#line 502 "InputParser/InputParser.yy"
    {
	(yyval.bnode) = currentBD->new_node((yyvsp[(1) - (3)].bnode),  (yyvsp[(3) - (3)].bnode), bool_node::AND);
}
    break;

  case 74:
#line 505 "InputParser/InputParser.yy"
    {
	(yyval.bnode) = currentBD->new_node((yyvsp[(1) - (3)].bnode),  (yyvsp[(3) - (3)].bnode), bool_node::OR);	
}
    break;

  case 75:
#line 508 "InputParser/InputParser.yy"
    { 	
	(yyval.bnode) = currentBD->new_node((yyvsp[(1) - (3)].bnode),  (yyvsp[(3) - (3)].bnode), bool_node::OR);	
}
    break;

  case 76:
#line 511 "InputParser/InputParser.yy"
    {	
	(yyval.bnode) = currentBD->new_node((yyvsp[(1) - (3)].bnode),  (yyvsp[(3) - (3)].bnode), bool_node::XOR);	
}
    break;

  case 77:
#line 514 "InputParser/InputParser.yy"
    {	
	bool_node* tmp = currentBD->new_node((yyvsp[(1) - (3)].bnode),  (yyvsp[(3) - (3)].bnode), bool_node::EQ);
	(yyval.bnode) = currentBD->new_node (tmp, NULL, bool_node::NOT);	
}
    break;

  case 78:
#line 518 "InputParser/InputParser.yy"
    { 			
	(yyval.bnode) = currentBD->new_node((yyvsp[(1) - (3)].bnode),  (yyvsp[(3) - (3)].bnode), bool_node::EQ);
}
    break;

  case 79:
#line 521 "InputParser/InputParser.yy"
    {
	(yyval.bnode) = currentBD->new_node((yyvsp[(3) - (4)].bnode), (yyvsp[(1) - (4)].bnode), bool_node::ARR_R);
}
    break;

  case 80:
#line 524 "InputParser/InputParser.yy"
    {
   
	//TUPLE_R_node* tn = dynamic_cast<TUPLE_R_node*>();
    
	//tn->idx = $4;
	(yyval.bnode) = currentBD->new_node((yyvsp[(1) - (5)].bnode), (yyvsp[(4) - (5)].intConst));
	
}
    break;

  case 81:
#line 532 "InputParser/InputParser.yy"
    {
	(yyval.bnode) = currentBD->new_node((yyvsp[(3) - (4)].bnode), currentBD->create_const((yyvsp[(1) - (4)].intConst)), bool_node::ARR_R);		
}
    break;

  case 82:
#line 535 "InputParser/InputParser.yy"
    {
	ARR_W_node* an = dynamic_cast<ARR_W_node*>(newNode(bool_node::ARR_W));
	an->getOldArr() = ( currentBD->get_node(*(yyvsp[(1) - (8)].strConst)) );
	an->getNewVal() = ( (yyvsp[(6) - (8)].bnode) );
	(yyval.bnode) = currentBD->new_node((yyvsp[(4) - (8)].bnode), NULL, an);	
	delete (yyvsp[(1) - (8)].strConst);
}
    break;

  case 83:
#line 542 "InputParser/InputParser.yy"
    {
	ARR_W_node* an = dynamic_cast<ARR_W_node*>(newNode(bool_node::ARR_W));
	an->getOldArr() = ( currentBD->create_const((yyvsp[(1) - (8)].intConst)) );
	an->getNewVal() = ( (yyvsp[(6) - (8)].bnode) );
	(yyval.bnode) = currentBD->new_node((yyvsp[(4) - (8)].bnode), NULL, an);		
}
    break;

  case 84:
#line 548 "InputParser/InputParser.yy"
    {
	int pushval = 0;
	
	list<bool_node*>* childs = (yyvsp[(2) - (6)].nList);
	list<bool_node*>::reverse_iterator it = childs->rbegin();
	int bigN = childs->size();
	ARRACC_node* an = dynamic_cast<ARRACC_node*>(newNode(bool_node::ARRACC, bigN));
	for(int i=0; i<bigN; ++i, ++it){
		an->arguments(i) = (*it);
	}		
	Assert((yyvsp[(5) - (6)].bnode) != NULL, "2: THIS CAN'T HAPPEN!!");	
	(yyval.bnode) = currentBD->new_node((yyvsp[(5) - (6)].bnode), NULL,  an);
	delete childs;	
}
    break;

  case 85:
#line 562 "InputParser/InputParser.yy"
    {
	

	list<bool_node*>* childs = (yyvsp[(2) - (3)].nList);
	list<bool_node*>::reverse_iterator it = childs->rbegin();
	int bigN = childs->size();
	ARR_CREATE_node* an = dynamic_cast<ARR_CREATE_node*>(newNode(bool_node::ARR_CREATE, bigN));
    
	for(int i=0; i<bigN; ++i, ++it){
		an->arguments(i) = (*it);
	}	
	if(bigN > 0){
		if(an->arguments(0)->getOtype() == OutType::FLOAT ){
			(yyval.bnode) = currentBD->new_node(currentBD->create_const(0.0), NULL, an); 
		}else{
			(yyval.bnode) = currentBD->new_node(currentBD->create_const(0), NULL, an); 
		}

	}else{
		(yyval.bnode) = currentBD->new_node(currentBD->create_const(0), NULL, an); 
	}	
	delete childs;
}
    break;

  case 86:
#line 585 "InputParser/InputParser.yy"
    {

	

	list<bool_node*>* childs = (yyvsp[(5) - (6)].nList);
	list<bool_node*>::reverse_iterator it = childs->rbegin();
	
	int bigN = childs->size();
	TUPLE_CREATE_node* an = dynamic_cast<TUPLE_CREATE_node*>(newNode(bool_node::TUPLE_CREATE, bigN));	
	for(int i=0; i<bigN; ++i, ++it){
		an->set_parent(i, *it);
	}
    an->setName(*(yyvsp[(2) - (6)].strConst));
	(yyval.bnode) = currentBD->new_node(NULL, NULL, an); 
	delete childs;
}
    break;

  case 87:
#line 601 "InputParser/InputParser.yy"
    {
	
	list<bool_node*>* childs = (yyvsp[(2) - (3)].nList);
	list<bool_node*>::reverse_iterator it = childs->rbegin();
	int bigN = childs->size();
	ACTRL_node* an = dynamic_cast<ACTRL_node*>(newNode(bool_node::ACTRL, bigN));
	
	for(int i=0; i<bigN; ++i, ++it){
		an->set_parent(i, *it);
	}		
	(yyval.bnode) = currentBD->new_node(NULL, NULL, an); 
	delete childs;
}
    break;

  case 88:
#line 615 "InputParser/InputParser.yy"
    {
	(yyval.bnode) = currentBD->new_node((yyvsp[(1) - (3)].bnode),  (yyvsp[(3) - (3)].bnode), bool_node::PLUS); 	
}
    break;

  case 89:
#line 619 "InputParser/InputParser.yy"
    {	
	(yyval.bnode) = currentBD->new_node((yyvsp[(1) - (3)].bnode),  (yyvsp[(3) - (3)].bnode), bool_node::DIV); 	
}
    break;

  case 90:
#line 623 "InputParser/InputParser.yy"
    {	
	(yyval.bnode) = currentBD->new_node((yyvsp[(1) - (3)].bnode),  (yyvsp[(3) - (3)].bnode), bool_node::MOD); 	
}
    break;

  case 91:
#line 627 "InputParser/InputParser.yy"
    {
	(yyval.bnode)= currentBD->new_node((yyvsp[(1) - (3)].bnode),  (yyvsp[(3) - (3)].bnode), bool_node::TIMES);
}
    break;

  case 92:
#line 630 "InputParser/InputParser.yy"
    {
	bool_node* neg1 = currentBD->new_node((yyvsp[(3) - (3)].bnode), NULL, bool_node::NEG);
	(yyval.bnode) = currentBD->new_node((yyvsp[(1) - (3)].bnode), neg1, bool_node::PLUS); 	
}
    break;

  case 93:
#line 634 "InputParser/InputParser.yy"
    {
	
	(yyval.bnode) = currentBD->new_node((yyvsp[(3) - (3)].bnode), (yyvsp[(1) - (3)].bnode), bool_node::LT);     
}
    break;

  case 94:
#line 638 "InputParser/InputParser.yy"
    {
	(yyval.bnode) = currentBD->new_node((yyvsp[(1) - (3)].bnode), (yyvsp[(3) - (3)].bnode), bool_node::LT);
}
    break;

  case 95:
#line 641 "InputParser/InputParser.yy"
    {
	bool_node* tmp = currentBD->new_node((yyvsp[(1) - (3)].bnode), (yyvsp[(3) - (3)].bnode), bool_node::LT);
	(yyval.bnode) = currentBD->new_node(tmp, NULL, bool_node::NOT);
}
    break;

  case 96:
#line 645 "InputParser/InputParser.yy"
    {
	bool_node* tmp = currentBD->new_node((yyvsp[(3) - (3)].bnode), (yyvsp[(1) - (3)].bnode), bool_node::LT);
	(yyval.bnode) = currentBD->new_node(tmp, NULL, bool_node::NOT);
}
    break;

  case 97:
#line 649 "InputParser/InputParser.yy"
    {
	ARRACC_node* an = dynamic_cast<ARRACC_node*>(newNode(bool_node::ARRACC, 2));
	bool_node* yesChild =((yyvsp[(3) - (5)].bnode));
	bool_node* noChild = ((yyvsp[(5) - (5)].bnode));
	an->arguments(0) = ( noChild );
	an->arguments(1) = ( yesChild );	
	(yyval.bnode) = currentBD->new_node((yyvsp[(1) - (5)].bnode), NULL, an); 	
}
    break;

  case 98:
#line 660 "InputParser/InputParser.yy"
    { /* Empty */  	(yyval.nList) = new list<bool_node*>();	}
    break;

  case 99:
#line 661 "InputParser/InputParser.yy"
    {

//The signs are already in the stack by default. All I have to do is not remove them.
	if((yyvsp[(1) - (2)].bnode) != NULL){
		(yyvsp[(2) - (2)].nList)->push_back( (yyvsp[(1) - (2)].bnode) );
	}else{
		(yyvsp[(2) - (2)].nList)->push_back( NULL );
	}
	(yyval.nList) = (yyvsp[(2) - (2)].nList);
}
    break;

  case 100:
#line 672 "InputParser/InputParser.yy"
    {
	(yyval.sList) = new list<string*>();	
	(yyval.sList)->push_back( (yyvsp[(1) - (1)].strConst));
}
    break;

  case 101:
#line 676 "InputParser/InputParser.yy"
    {
	(yyval.sList) = (yyvsp[(2) - (2)].sList);
	(yyval.sList)->push_back( (yyvsp[(1) - (2)].strConst));
}
    break;

  case 102:
#line 681 "InputParser/InputParser.yy"
    {
	(yyval.bnode) = currentBD->create_const((yyvsp[(1) - (1)].intConst));
}
    break;

  case 103:
#line 684 "InputParser/InputParser.yy"
    {
	(yyval.bnode) = currentBD->create_const((yyvsp[(1) - (1)].doubleConst));
}
    break;

  case 104:
#line 688 "InputParser/InputParser.yy"
    {
    
	list<bool_node*>* params = (yyvsp[(7) - (16)].nList);
	if(false && params->size() == 0){

        (yyval.bnode) = currentBD->create_inputs(-1,OutType::getTuple(*(yyvsp[(4) - (16)].strConst)), *(yyvsp[(1) - (16)].strConst));

		delete (yyvsp[(1) - (16)].strConst);
	}else{	
		string& fname = *(yyvsp[(1) - (16)].strConst);
		list<bool_node*>::reverse_iterator parit = params->rbegin();
		UFUN_node* ufun = UFUN_node::create(fname, params->size());
		ufun->outname = *(yyvsp[(13) - (16)].strConst);
		int fgid = (yyvsp[(15) - (16)].intConst);
		ufun->fgid = fgid;
		bool_node* pCond;	
		for(int i=0 ; parit != params->rend(); ++parit, ++i){
            ufun->arguments(i) = (*parit);
        }
        pCond = (yyvsp[(10) - (16)].bnode);


        ufun->set_nbits( 0 );
        ufun->set_tupleName(*(yyvsp[(4) - (16)].strConst));
		
		
		//ufun->name = (currentBD->new_name(fname));
		(yyval.bnode) = currentBD->new_node(pCond, NULL, ufun);

        delete (yyvsp[(1) - (16)].strConst);
		delete (yyvsp[(13) - (16)].strConst);
	}
	delete (yyvsp[(7) - (16)].nList);

}
    break;

  case 105:
#line 723 "InputParser/InputParser.yy"
    {
	
	list<bool_node*>* params = (yyvsp[(6) - (15)].nList);
	if(false && params->size() == 0){
		if( (yyvsp[(3) - (15)].variableType) == INT){
			(yyval.bnode) = currentBD->create_inputs( 2 /*NINPUTS*/, OutType::INT , *(yyvsp[(1) - (15)].strConst)); 
		}else{
			if((yyvsp[(3) - (15)].variableType)==FLOAT){
				(yyval.bnode) = currentBD->create_inputs(2,OutType::FLOAT, *(yyvsp[(1) - (15)].strConst));
			}else{
				(yyval.bnode) = currentBD->create_inputs(-1,OutType::BOOL, *(yyvsp[(1) - (15)].strConst));
			}
		}
		delete (yyvsp[(1) - (15)].strConst);
	}else{	
		string& fname = *(yyvsp[(1) - (15)].strConst);
		list<bool_node*>::reverse_iterator parit = params->rbegin();
		UFUN_node* ufun = UFUN_node::create(fname, params->size());
		ufun->outname = *(yyvsp[(12) - (15)].strConst);
		int fgid = (yyvsp[(14) - (15)].intConst);
		ufun->fgid = fgid;	
		bool_node* pCond;	

        for(int i=0 ; parit != params->rend(); ++parit, ++i){
            ufun->arguments(i) = (*parit);
        }
        pCond = (yyvsp[(9) - (15)].bnode);

		
		if( (yyvsp[(3) - (15)].variableType) == INT || (yyvsp[(3) - (15)].variableType)==INT_ARR){
			ufun->set_nbits( 2 /*NINPUTS*/  );
		}else{	
			ufun->set_nbits( 1  );
		}
		if((yyvsp[(3) - (15)].variableType) == INT_ARR || (yyvsp[(3) - (15)].variableType)==BIT_ARR){
			ufun->makeArr();
		}
		
		//ufun->name = (currentBD->new_name(fname));
		(yyval.bnode) = currentBD->new_node(pCond, NULL, ufun);

		
		delete (yyvsp[(1) - (15)].strConst);
		delete (yyvsp[(12) - (15)].strConst);
	}
	delete (yyvsp[(6) - (15)].nList);
}
    break;

  case 106:
#line 771 "InputParser/InputParser.yy"
    {		
		(yyval.bnode) = currentBD->new_node((yyvsp[(2) - (2)].bnode), NULL, bool_node::NEG);				
}
    break;

  case 107:
#line 774 "InputParser/InputParser.yy"
    { 
	(yyval.bnode) = currentBD->new_node((yyvsp[(2) - (2)].bnode), NULL, bool_node::NOT);		    
}
    break;

  case 108:
#line 778 "InputParser/InputParser.yy"
    { 
						(yyval.bnode) = (yyvsp[(2) - (3)].bnode); 
						}
    break;

  case 109:
#line 781 "InputParser/InputParser.yy"
    { 			
			(yyval.bnode) = currentBD->get_node(*(yyvsp[(1) - (1)].strConst));
			delete (yyvsp[(1) - (1)].strConst);				
			 
		}
    break;

  case 110:
#line 786 "InputParser/InputParser.yy"
    {		
	(yyval.bnode) = currentBD->create_controls(-1, *(yyvsp[(2) - (3)].strConst));
	delete (yyvsp[(2) - (3)].strConst);
}
    break;

  case 111:
#line 790 "InputParser/InputParser.yy"
    {
	int nctrls = (yyvsp[(3) - (4)].intConst);
	if(overrideNCtrls){
		nctrls = NCTRLS;
	}
	(yyval.bnode) = currentBD->create_controls(nctrls, *(yyvsp[(2) - (4)].strConst));
	delete (yyvsp[(2) - (4)].strConst);
}
    break;

  case 112:
#line 798 "InputParser/InputParser.yy"
    {
	(yyval.bnode) = currentBD->create_controls((yyvsp[(3) - (5)].intConst), *(yyvsp[(2) - (5)].strConst));
	delete (yyvsp[(2) - (5)].strConst);

}
    break;

  case 113:
#line 803 "InputParser/InputParser.yy"
    {
	(yyval.bnode) = currentBD->create_controls(-1, *(yyvsp[(2) - (4)].strConst), false, true);
	delete (yyvsp[(2) - (4)].strConst);
}
    break;

  case 114:
#line 807 "InputParser/InputParser.yy"
    {
	(yyval.bnode) = currentBD->create_controls((yyvsp[(3) - (5)].intConst), *(yyvsp[(2) - (5)].strConst), false, true);
	delete (yyvsp[(2) - (5)].strConst);
}
    break;

  case 115:
#line 811 "InputParser/InputParser.yy"
    {
  (yyval.bnode) = currentBD->create_controls(-1, *(yyvsp[(2) - (4)].strConst), false, true, false, -1, true);
  delete (yyvsp[(2) - (4)].strConst);
}
    break;

  case 116:
#line 815 "InputParser/InputParser.yy"
    {
	(yyval.bnode) = currentBD->create_controls(-1, *(yyvsp[(3) - (4)].strConst), true);
	delete (yyvsp[(3) - (4)].strConst);
}
    break;

  case 117:
#line 819 "InputParser/InputParser.yy"
    {
	int nctrls = (yyvsp[(4) - (5)].intConst);
	if(overrideNCtrls){
		nctrls = NCTRLS;
	}
	(yyval.bnode) = currentBD->create_controls(nctrls, *(yyvsp[(3) - (5)].strConst), true);
	delete (yyvsp[(3) - (5)].strConst);
}
    break;

  case 118:
#line 827 "InputParser/InputParser.yy"
    {
	(yyval.bnode) = currentBD->create_controls((yyvsp[(4) - (6)].intConst), *(yyvsp[(3) - (6)].strConst), true);
	delete (yyvsp[(3) - (6)].strConst);

}
    break;

  case 119:
#line 832 "InputParser/InputParser.yy"
    {
	(yyval.bnode) = currentBD->create_controls(-1, *(yyvsp[(7) - (8)].strConst), false, false, true, (yyvsp[(2) - (8)].intConst));
  ((CTRL_node*) (yyval.bnode))->setPredecessors(*(yyvsp[(4) - (8)].sVector));
	delete (yyvsp[(7) - (8)].strConst);
}
    break;

  case 120:
#line 837 "InputParser/InputParser.yy"
    {
	int nctrls = (yyvsp[(8) - (9)].intConst);
	if(overrideNCtrls){
		nctrls = NCTRLS;
	}
	(yyval.bnode) = currentBD->create_controls(nctrls, *(yyvsp[(7) - (9)].strConst), false, false, true, (yyvsp[(2) - (9)].intConst));
  ((CTRL_node*) (yyval.bnode))->setPredecessors(*(yyvsp[(4) - (9)].sVector));
	delete (yyvsp[(7) - (9)].strConst);
}
    break;

  case 121:
#line 846 "InputParser/InputParser.yy"
    {
	(yyval.bnode) = currentBD->create_controls((yyvsp[(8) - (10)].intConst), *(yyvsp[(7) - (10)].strConst), false, false, true, (yyvsp[(2) - (10)].intConst));
  ((CTRL_node*) (yyval.bnode))->setPredecessors(*(yyvsp[(4) - (10)].sVector));
	delete (yyvsp[(7) - (10)].strConst);
}
    break;

  case 122:
#line 853 "InputParser/InputParser.yy"
    { /* Empty */  	(yyval.sVector) = new vector<string>();	}
    break;

  case 123:
#line 854 "InputParser/InputParser.yy"
    {
  (yyvsp[(1) - (2)].sVector)->push_back(*(yyvsp[(2) - (2)].strConst));
	(yyval.sVector) = (yyvsp[(1) - (2)].sVector);
}
    break;

  case 124:
#line 859 "InputParser/InputParser.yy"
    { (yyval.intConst) = (yyvsp[(1) - (1)].intConst); }
    break;

  case 125:
#line 860 "InputParser/InputParser.yy"
    { (yyval.intConst) = (yyvsp[(1) - (3)].intConst) + (yyvsp[(3) - (3)].intConst); }
    break;

  case 126:
#line 861 "InputParser/InputParser.yy"
    { (yyval.intConst) = (yyvsp[(1) - (3)].intConst) - (yyvsp[(3) - (3)].intConst); }
    break;

  case 127:
#line 863 "InputParser/InputParser.yy"
    { (yyval.intConst) = (yyvsp[(1) - (1)].intConst); }
    break;

  case 128:
#line 864 "InputParser/InputParser.yy"
    { (yyval.intConst) = (yyvsp[(2) - (3)].intConst); }
    break;

  case 129:
#line 865 "InputParser/InputParser.yy"
    { (yyval.intConst) = (yyvsp[(1) - (3)].intConst) * (yyvsp[(3) - (3)].intConst); }
    break;

  case 130:
#line 866 "InputParser/InputParser.yy"
    { Assert( (yyvsp[(3) - (3)].intConst) != 0, "You are attempting to divide by zero !!");
							      (yyval.intConst) = (yyvsp[(1) - (3)].intConst) / (yyvsp[(3) - (3)].intConst); }
    break;

  case 131:
#line 868 "InputParser/InputParser.yy"
    { Assert( (yyvsp[(3) - (3)].intConst) != 0, "You are attempting to mod by zero !!");
							      (yyval.intConst) = (yyvsp[(1) - (3)].intConst) % (yyvsp[(3) - (3)].intConst); }
    break;

  case 132:
#line 872 "InputParser/InputParser.yy"
    {  (yyval.intConst) = (yyvsp[(1) - (1)].intConst); }
    break;

  case 133:
#line 873 "InputParser/InputParser.yy"
    {  (yyval.intConst) = -(yyvsp[(2) - (2)].intConst); }
    break;

  case 134:
#line 876 "InputParser/InputParser.yy"
    {  (yyval.intConst) = (yyvsp[(1) - (1)].intConst); }
    break;

  case 135:
#line 877 "InputParser/InputParser.yy"
    { (yyval.intConst) = 1; }
    break;

  case 136:
#line 878 "InputParser/InputParser.yy"
    { (yyval.intConst) = 0; }
    break;

  case 137:
#line 880 "InputParser/InputParser.yy"
    { (yyval.strConst)=(yyvsp[(1) - (1)].strConst); }
    break;


/* Line 1267 of yacc.c.  */
#line 2976 "InputParser.cpp"
      default: break;
    }
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;


  /* Now `shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*------------------------------------.
| yyerrlab -- here on detecting error |
`------------------------------------*/
yyerrlab:
  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (yyscanner, YY_("syntax error"));
#else
      {
	YYSIZE_T yysize = yysyntax_error (0, yystate, yychar);
	if (yymsg_alloc < yysize && yymsg_alloc < YYSTACK_ALLOC_MAXIMUM)
	  {
	    YYSIZE_T yyalloc = 2 * yysize;
	    if (! (yysize <= yyalloc && yyalloc <= YYSTACK_ALLOC_MAXIMUM))
	      yyalloc = YYSTACK_ALLOC_MAXIMUM;
	    if (yymsg != yymsgbuf)
	      YYSTACK_FREE (yymsg);
	    yymsg = (char *) YYSTACK_ALLOC (yyalloc);
	    if (yymsg)
	      yymsg_alloc = yyalloc;
	    else
	      {
		yymsg = yymsgbuf;
		yymsg_alloc = sizeof yymsgbuf;
	      }
	  }

	if (0 < yysize && yysize <= yymsg_alloc)
	  {
	    (void) yysyntax_error (yymsg, yystate, yychar);
	    yyerror (yyscanner, yymsg);
	  }
	else
	  {
	    yyerror (yyscanner, YY_("syntax error"));
	    if (yysize != 0)
	      goto yyexhaustedlab;
	  }
      }
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse look-ahead token after an
	 error, discard it.  */

      if (yychar <= YYEOF)
	{
	  /* Return failure if at end of input.  */
	  if (yychar == YYEOF)
	    YYABORT;
	}
      else
	{
	  yydestruct ("Error: discarding",
		      yytoken, &yylval, yyscanner);
	  yychar = YYEMPTY;
	}
    }

  /* Else will try to reuse look-ahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule which action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;	/* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (yyn != YYPACT_NINF)
	{
	  yyn += YYTERROR;
	  if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
	    {
	      yyn = yytable[yyn];
	      if (0 < yyn)
		break;
	    }
	}

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
	YYABORT;


      yydestruct ("Error: popping",
		  yystos[yystate], yyvsp, yyscanner);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  if (yyn == YYFINAL)
    YYACCEPT;

  *++yyvsp = yylval;


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#ifndef yyoverflow
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (yyscanner, YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEOF && yychar != YYEMPTY)
     yydestruct ("Cleanup: discarding lookahead",
		 yytoken, &yylval, yyscanner);
  /* Do not reclaim the symbols of the rule which action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
		  yystos[*yyssp], yyvsp, yyscanner);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  /* Make sure YYID is used.  */
  return YYID (yyresult);
}


#line 882 "InputParser/InputParser.yy"



void Inityyparse(){

	 	
}

void yyerror( void* yyscanner, const char* c){
	Assert(false, (char *)c); 
}


int isatty(int i){



return 1;
}

