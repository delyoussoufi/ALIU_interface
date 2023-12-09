import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ArtDataService } from '../art-data.service';

@Component({
  selector: 'app-art-object-list',
  templateUrl: './art-object-list.component.html',
  styleUrls: ['./art-object-list.component.css']
})
export class ArtObjectListComponent implements OnInit {
  artObjects: any[] = [];

  constructor(
    private artDataService: ArtDataService,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      const query = params['query'];
      if (query) {
        this.artDataService.searchArtObjects(query).subscribe(data => {
          this.artObjects = data;
        }, error => {
          console.error('Error fetching art objects:', error);
        });
      }
    });
  }

  // Correctly defined method
  objectKeys(obj: any): string[] {
    return Object.keys(obj);
  }
}