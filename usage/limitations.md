---
title: "Limitations"
description: "List the limitations of the BPTK-Py framework."
keywords: "agent-based modeling, abm, bptk, bptk-py, python, business simulation"
---

# Limitations


Currently the BPTK_Py framework is geared towards our own need and has a
number of limitations. We are more than happy to extend the framework to
suit YOUR need, so please let us what you need so that we can prioritize
our activities. You can reach us at <support@transentis.com>

Here are the known limitations:

-   Currently the simulator only supports the Euler method, Runge-Kutta
    Integration is not supported.
-   The SD model transpiler for XMILE models only supports regular
    stocks, flows, biflows and converters. Non-negative stocks and
    discrete modeling elements (such as ovens and conveyors) are not
    supported.
-   Subranges for arrays are currently not supported.
-   The inner product operator for arrays is currently not supported.
-   Special notations for arrays (e.g. N1:N2 and @) are currently not
    supported.
-   The random number operators (LOGNORMAL, LOGISTIC etc.) support seed
    but uses the Python seed and random number generator as the Stella
    Architect random number function is not open source. Secondly, these
    operators only support the mandatory arguments (usually
    mean/scale/stddev) as given in [in the Stella
    documentation](https://www.iseesystems.com/resources/help/v2/default.htm#08-Reference/07-Builtins/Statistical_builtins.htm)
-   The following table gives an overview of all XMILE builtins, whether
    they are supported by the SD model transpiler for XMILE and their
    equivalent in the SD DSL library -- blank cells indicate that the
    operator is currently not supported. We are working hard to ensure
    support for all operators is included ASAP. Built-ins pertaining to
    discrete elements are not listed.

  Built-In        SD model transpiler   SD DSL equivalent
  --------------- --------------------- -----------------------------------------
  ABS             x                     abs
  AND             x                     And
  ARCCOS          x                     arccos
  ARCSIN          x                     arcsin
  ARCTAN          x                     arctan
  BETA            x                     beta
  BINOMIAL        x                     binomial
  COMBINATIONS    x                     combinations
  COS             x                     cos
  CGROWTH         x                     \-
  CLOCKTIME       x                     \-
  COSWAVE         x                     coswave
  COUNTER         x                     \-
  DELAY           x                     \-
  DELAY1          x                     \-
  DELAY3          x                     \-
  DELAYN          x                     \-
  DERIVN          x                     \-
  DT              x                     dt
  ELSE            x                     If
  EXP             x                     exp
  EXPRND          x                     exprnd
  ENDVAL          x                     \-
  FACTORIAL       x                     factorial
  FORCST          x                     \-
  FV              x                     \-
  GAMMA           x                     gamma
  GAMMALN         x                     gammaln
  GEOMETRIC       x                     geometric
  HISTORY         x                     \-
  IF              x                     If
  INF             x                     Inf
  INTERPOLATE     x                     \-
  INIT            x                     \-
  INT             x                     \-
  INVNORM         x                     \-
  IRR             x                     \-
  LOG10           x                     \-
  LOGISTIC        x                     logistic
  LOGNORMAL       x                     lognormal
  LOOKUP          x                     lookup
  LOOKUPAREA      x                     \-
  LOOKUPINV       x                     \-
  LN              x                     \-
  MAX             x                     max
  MEAN            x                     \-
  MIN             x                     min
  MOD             x                     \% (simply use the Python mod operator)
  MONTECARLO      x                     montecarlo
  NAN             x                     nan
  NEGBINOMIAL     x                     \-
  NORMAL          x                     \-
  NORMALCDF       x                     \-
  NOT             x                     Not
  NPV             x                     \-
  OR              x                     Or
  PARETO          x                     pareto
  PERCENT         x                     \-
  PERMUTATIONS    x                     permutations
  PI              x                     pi
  PMT             x                     \-
  POISSON         x                     poisson
  PREVIOUS        x                     \-
  PULSE           x                     pulse
  PV              x                     \-
  PROD            x                     \-
  RANDOM          x                     random
  RANK            x                     \-
  RAMP            x                     \-
  REWORK          \-                    \-
  ROUND           x                     round
  ROOTN           x                     \-
  RUNCOUNT        \-                    \-
  SAFEDIV         x                     \-
  SELF            x                     \-
  SENSIRUNCOUNT   \-                    \-
  SIN             x                     sin
  SINWAVE         x                     sinwave
  SIZE            x                     \-
  SMTH1           x                     smooth
  SMTH3           x                     \-
  SMTHN           x                     \-
  SQRT            x                     sqrt
  STARTTIME       x                     starttime
  STDDEV          x                     \-
  STEP            x                     step
  STOPTIME        x                     stoptime
  SUM             x                     \-
  TAN             x                     tan
  THEN            x                     if
  TIME            x                     time
  TREND           x                     trend
  TRIANGULAR      x                     triangular
  UNIFORM         x                     uniform
  WEIBULL         x                     weibull