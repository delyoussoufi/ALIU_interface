// import { Component } from '@angular/core';
// import { Router } from '@angular/router';

// @Component({
//   selector: 'app-search',
//   templateUrl: './search.component.html',
//   styleUrls: ['./search.component.css']
// })
// export class SearchComponent {
//   searchTerm: string = '';

//   constructor(private router: Router) { }

//   searchArtObjects(): void {
//     if (this.searchTerm) {
//       this.router.navigate(['/art-objects'], { queryParams: { query: this.searchTerm } });
//     }
//   }
// }


import { Component, EventEmitter, Output } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-search', // Replace with your actual selector
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent {
  searchTerm: string = '';
  @Output() searchPerformed = new EventEmitter<void>(); // Event emitter for search action

  constructor(private router: Router) { }

  searchArtObjects(): void {
    if (this.searchTerm) {
      // Perform the navigation based on the search term
      this.router.navigate(['/art-objects'], { queryParams: { query: this.searchTerm } });

      // Emit the event to notify the parent component
      this.searchPerformed.emit();
    }
  }
}

