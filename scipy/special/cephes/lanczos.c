/*  (C) Copyright John Maddock 2006.
 *  Use, modification and distribution are subject to the
 *  Boost Software License, Version 1.0. (See accompanying file
 *  LICENSE_1_0.txt or copy at https://www.boost.org/LICENSE_1_0.txt)
 */

/* Scipy changes:
 * - 06-22-2016: Removed all code not related to double precision and
 *   ported to c for use in Cephes
 */

#include "mconf.h"
#include "lanczos.h"

double lanczos_sum_expg_scaled(double x)
{
    return ratevl(x, lanczos_sum_expg_scaled_num,
		  sizeof(lanczos_sum_expg_scaled_num) / sizeof(lanczos_sum_expg_scaled_num[0]) - 1,
		  lanczos_sum_expg_scaled_denom,
		  sizeof(lanczos_sum_expg_scaled_denom) / sizeof(lanczos_sum_expg_scaled_denom[0]) - 1);
}

