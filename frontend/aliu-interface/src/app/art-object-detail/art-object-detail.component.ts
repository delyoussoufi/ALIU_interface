import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ArtDataService } from '../art-data.service';

@Component({
  selector: 'app-art-object-detail',
  templateUrl: './art-object-detail.component.html',
  styleUrls: ['./art-object-detail.component.css']
})
export class ArtObjectDetailComponent implements OnInit {
  artObject: any;
  ownerships: any[] = [];
  artObjectId: string = '';

  constructor(
    private route: ActivatedRoute,
    private artDataService: ArtDataService
  ) { }

  ngOnInit(): void {
    this.artObjectId = this.route.snapshot.paramMap.get('id')!;
    this.fetchArtObjectDetails();
  }

  fetchArtObjectDetails(): void {
    // Fetch art object details
    this.artDataService.getArtObjectById(this.artObjectId).subscribe(
      data => {
        this.artObject = data;
      },
      error => {
        console.error('There was an error fetching the art object details!', error);
      }
    );

    // Fetch ownerships
    this.artDataService.getOwnerships(this.artObjectId).subscribe(
      data => {
        this.ownerships = data;
      },
      error => {
        console.error('There was an error fetching ownerships!', error);
      }
    );
  }

  objectKeys(obj: any): string[] {
    return Object.keys(obj);
  }

  formatKey(key: string): string {
    // Format the key for display
    return key.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase());
  }

}
