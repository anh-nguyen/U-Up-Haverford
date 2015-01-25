/*function filter_study(x) {
	if (x.checked == true) {
		$( "li" ).each(function( y ) {
			if ( $( this ).is( "#study" ) ) {
				this.getElementById("#study").style.display='block';
			}
			})
		} //end each		 
	else {
		$( "li" ).each(function( ) {
                        if ( $( this ).is( "#study" ) ) {
                                document.getElementById("#study").style.display='none';
			};

	})
}	
}
*/

function filter_study(x) {
        if (x.checked == true) {
                $('.study').show();
        }
        else {
                 $('.study').hide();
	}	
}

function filter_food(x) {
        if (x.checked == true) {
                $('.get_food').show();

        }
        else {
                 $('.get_food').hide();
        }
}


function filter_hangout(x) {
        if (x.checked == true) {
                $('.hang_out').show();
        }
        else {
                 $('.hang_out').hide();
        }
}

